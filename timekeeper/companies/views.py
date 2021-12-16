from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import AddCompanyForm

import logging
import boto3
from botocore.exceptions import ClientError

from pathlib import Path

path = Path(__file__).parent / "testfile.txt"

# Create your views here.

#def index(request):
 #   '''The home page for Learning Long'''
  #  return render(request,'companies/index.html')

##################################################################################
#   List all of the Clients Stored on Dynamo DB Database
##################################################################################
def admin_company_list(request):
   
    region = 'us-east-1'
    table_name ="timekeeper_clients"
    dynamo_db_clients = list ()
    
    
    #   create a dictionary to pass all of the arguments
    table_args = {'region':region,'table_name': table_name}
    
    dynamo_client = DynamoDB()
    client_list_resp = dynamo_client.get_items_A_to_Z(table_args)
    
    print('PRINTING THE RESPONSE FOR THE LIST')
    print(client_list_resp)
    
    # iterate over the returned client list and extract username and email and Status
    for client in client_list_resp:
        client_record = {
            'eircode':client['eircode'],
            'company_name':client['company_name'],
            'industry': client['industry']
        }
        dynamo_db_clients.append(client_record)
    
    args = {
        'heading':'Client Listing' ,'dynamo_db_clients':dynamo_db_clients
    }
    return render(request,'companies/admin_company_list.html',args)

##################################################################################
#   Add a client to Dynamo DB
##################################################################################
def admin_company_add(request):
    region = 'us-east-1'
    
    #   CHECK IF THE FORM WAS SUBMITTED
    #   If so, then read in the contents of the form
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        
        #   Check if the form contents is valid
        if form.is_valid():
            company_name = request.POST['company_name']
            industry  = request.POST['industry']
            eircode  = request.POST['eircode']
            
            item = {'company_name': company_name,'industry':industry,'eircode': eircode}
            
            #   upload CLIENT to DYNAMO DB via use of a class
            dynamo_client = DynamoDB()
            table_name="timekeeper_clients"
            #item = {
           #     "company_name": company_name,
           #     "industry" : industry,
           #     "eircode": eircode
           # }
            uploaded = dynamo_client.add_a_client(region, table_name, item)
            
            print('client was uploaded?')
            print(uploaded)
            
            #   CHECK if the UPLOAD WAS SUCCESSFUL
            #   If yes, diplay the list 
            #   If no, display error
            if uploaded:
                return redirect(reverse('companies:admin_company_list'))
            else:
                return redirect(reverse('companies:admin_company_add_error'))
    else:        
        
        #   If the page was just browsed to
        #   Then load an empty form
        form = AddCompanyForm()
    
        args = {'heading' : 'Add Client', 'form': form}
        return render(request,'companies/admin_company_add.html',args)

##################################################################################
#   Display ERROR Screen
##################################################################################
def admin_company_add_error(request):
    args = {'heading' : 'Upload Error'}
    return render(request,'cognito_user/admin_cognito_user_error.html',args)      



##################################################################################
#    DYNAMO DB CLASS USED FOR INTERACTING WITH COGNITO
##################################################################################
class DynamoDB:
    
    
    #   CREATE A TABLE ON DYNAMO DB
    def create_table(self, table_name, key_schema, attribute_definitions, provisioned_throughput, region):
        
        try:
            dynamodb_resource = boto3.resource("dynamodb", region_name=region)
            self.table = dynamodb_resource.create_table(TableName=table_name, KeySchema=key_schema, AttributeDefinitions=attribute_definitions,
                ProvisionedThroughput=provisioned_throughput)

            # Wait until the table exists.
            self.table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

        except ClientError as e:
            logging.error(e)
            return False
            
        return True
        
    #   UPLOAD AN ITEM TO THE SPECIFIED TABLE ON DYNAMO DB
    def add_a_client(self, region, table_name, item):
        try:
            dynamodb_resource = boto3.resource("dynamodb", region_name=region)
            table = dynamodb_resource.Table(table_name)
            table.put_item(Item=item)
        
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
    #   RETRIEVE A SPECIFIED ITEM FROM A DYNAMO DB TABLE
    def get_an_item(self,region, table_name, key):
        try:
            dynamodb_resource = boto3.resource("dynamodb", region_name=region)
            table = dynamodb_resource.Table(table_name)
            response = table.get_item(Key=key)
            items_list = response['Item']
            
        except ClientError as e:
            logging.error(e)
            
        return(items_list)
        
    #   RETRIEVE A LIST OF ITEMS FROM A DYNAMO DB TABLE
    def get_items_A_to_Z(self,table_args):
        region = table_args['region']
        table_name = table_args['table_name']
        
        print('in get_items_A_to_Z')
        print('region is '+region)
        print('table name is '+table_name)

        
        
        try:
            dynamodb_resource = boto3.resource("dynamodb", region_name=region)
            table = dynamodb_resource.Table(table_name)
            
            response = table.scan(
                TableName=table_name,
                Select='ALL_ATTRIBUTES'
		    )
            return(response['Items'])
            
        except ClientError as e:
            logging.error(e)
            return([{'error': 'list empty'}])
        