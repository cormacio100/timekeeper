from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.template.context_processors import csrf
from .forms import AddCognitoUserForm
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from botocore.exceptions import ClientError
from datetime import date
from django.conf import settings

import logging
import boto3 

############################################################################
# Welcome page for teh application
############################################################################
def index(request):
    return render(request,'index.html')

############################################################################
#   GENERAL User Landing page
############################################################################
def general_user(request):
    args = {'heading' : 'General User Task'}
    return render(request,'general_user.html',args)

############################################################################    
#   UPLOAD EXPENSES RELATED TO SPECIFIC CLIENT
############################################################################
def general_user_upload_expenses(request):
    args = {'heading' : 'Upload Expenses'}
    dynamo_db_clients = list ()
    
    ######################################################
    #   Retrieve the list of clients from Dynamo DB
    ######################################################
    region = 'us-east-1'
   
    dynamo_client = DynamoDBDemo()
    table_name="timekeeper_client_list"
    client_list_resp = dynamo_client.get_items_A_to_Z(region, table_name)
    
    print('PRINTING THE RESPONSE FOR THE LIST')
    print(client_list_resp)
    
    # iterate over the returned client list and extract username and email and Status
    for client in client_list_resp:
        client_record = {
            #'eircode':client['eircode'],
            'company_name':client['company_name'],
            'industry': client['industry'],
            'county': client['county'],
            'lat': client['lat'],
            'lng': client['lng'],
        }
        
        dynamo_db_clients.append(client_record)
    
    args.update({'dynamo_db_clients':dynamo_db_clients})
    args.update({'message':''})
    
    #########################################################
    #   Check if the form was submitted
    #   If yes then upload the file locally first
    #   then to S3
    #########################################################
    if request.method == 'POST' and request.FILES['myfile']:

        company_name = request.POST['company_name']
        expense_type = request.POST['expense_type']

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        try:
            #   Save the file locally
            file_name = fs.save(company_name.replace(" ", "_")+'__'+myfile.name.replace(" ", "_"), myfile)
            uploaded_file_url = fs.url(file_name)
            print('FILENAME IS : '+file_name)
            print('uploaded file url: '+uploaded_file_url)
       
            #########################################################
            #   UPLOAD the file to an S3 bucket
            #########################################################
            import os 
            object_key = file_name
            save_path = settings.MEDIA_ROOT
            complete_name = os.path.join(save_path, object_key)
            
            print('\t Uploading to S3 Bucket from '+complete_name)
            
            # Upload the file to S3
            s3_client = boto3.client('s3')
            try:
                bucket='timekeeperuploadbucket'
                
                print('bucket = '+bucket)
                
                if('travel'==expense_type):
                    #response = s3_client.upload_file(complete_name, bucket, object_key)
                    #upload_file('/tmp/' + filename, '<bucket-name>', 'folder/{}'.format(filename))
                    response = s3_client.upload_file(complete_name, bucket, 'travel/{}'.format(file_name))
                elif('food'==expense_type):
                    response = s3_client.upload_file(complete_name, bucket, 'food/{}'.format(file_name))
                elif('accomodation'==expense_type):
                    response = s3_client.upload_file(complete_name, bucket, 'accomodation/{}'.format(file_name))
                elif('equipment'==expense_type):
                    response = s3_client.upload_file(complete_name, bucket, 'equipment/{}'.format(file_name))
                else: 
                    response = s3_client.upload_file(complete_name, bucket, object_key)
                '''
                # an example of using the ExtraArgs optional parameter to set the ACL (access control list) value 'public-read' to the S3 object
                response = s3_client.upload_file(file_name, bucket, key, 
                    ExtraArgs={'ACL': 'public-read'})
                '''
                
                args.update({'message':'**Upload Successful**'})
                
            except ClientError as e:
                logging.error(e)
                args.update({'message':'**Upload UnSuccessful**'})
                
        except ClientError as e:
            logging.error(e)
            args.update({'message':'**Upload UnSuccessful**'})


        return render(
            request, 
            'general_user_upload_expenses.html',
            args, 
            {'uploaded_file_url': uploaded_file_url}
        )
    else:
        return render(request, 'general_user_upload_expenses.html',args)   
 
    
############################################################################   
#   ADMIN User Landing page
############################################################################
def admin_user(request):
    args = {'heading' : 'Admin Task'}
    return render(request,'admin_user.html',args)
  
############################################################################ 
#   LISTING PAGE FOR COGNITO USERS
############################################################################
def admin_cognito_user_list(request):
    cognito_users = list ()
    user_id = 0
    
    # retrieve the list of users 
    region = 'us-east-1'
    UserPoolId='us-east-1_412rcjhr9'
    
    #   create a dictionary to pass all of the arguments
    args = {'region':region,'UserPoolId': UserPoolId}

    #   create an object of the Cognito class to do lookups of Cognito
    cognitoClient = Cognito()
    user_list_resp = cognitoClient.list_users(args)

    # iterate over the returned users and extract username and email and Status
    for user in user_list_resp['Users']:
        user_record = {'user_id': user_id, 'username': user['Username'], 'userstatus': user['UserStatus'], 'email': None}
        
        for attr in user['Attributes']:
            if attr['Name'] == 'email':
                user_record['email'] = attr['Value']
                
        cognito_users.append(user_record)
        user_id += 1
        
    #   pass the values to the template
    args = {'heading':'Cognito Users','cognito_users': cognito_users}
    return render(request,'cognito_user/admin_cognito_user_list.html',args)
    
############################################################################    
#   FUNCTION Creates A Cognito User based on values entered in a form  
############################################################################
def admin_cognito_user_add(request):
    
    #   Check if the request comes from the Congito Add User Form
    if request.method == 'POST':
        #   Create a form instance and populate it with the request data
        form = AddCognitoUserForm(request.POST)
        
        #  Check if the form contents is valid
        if form.is_valid():

            #   retrieve the data and
            #   Upload the new user to COGNITO using the Cognito Class functions
            email = request.POST['email']
            password = request.POST['password']
            region = 'us-east-1'
            cognitoClientID = '2neea3tmqro25ir2ohamglv1be'
            
            #   create a dictionary to pass all of the arguments
            args = {'email':email,'password': password,'region':region,'cognitoClientID':cognitoClientID}
        
            cognitoClient = Cognito()
            response = cognitoClient.sign_up_user(args)
            
            #   reload the UPDATED list of cognito users
            return redirect(reverse('tk_users:admin_cognito_user_list'))
    else:  
        form = AddCognitoUserForm()
        
        args = {'heading' : 'Add User', 'form': form}
        args.update(csrf(request))

        return render(request,'cognito_user/admin_cognito_user_add.html',args)


############################################################################
#   CLASSES SECTION
############################################################################ 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    DynamoDB CLASS USED FOR INTERACTING WITH COGNITO
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class DynamoDBDemo:
    
    ############################################################################
    #   Create a Table in DYNAMO DB
    ############################################################################
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

    ############################################################################
    #   Store an item to Dynamo DB table
    ############################################################################
    def store_an_item(self, region, table_name, item):
        try:
            dynamodb_resource = boto3.resource("dynamodb", region_name=region)
            table = dynamodb_resource.Table(table_name)
            table.put_item(Item=item)
        
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
    ############################################################################
    #   retrieve an item from Dynamo DB table
    ############################################################################        
    def get_an_item(self,region, table_name, key):
        try:
            dynamodb_resource = boto3.resource("dynamodb", region_name=region)
            table = dynamodb_resource.Table(table_name)
            response = table.get_item(Key=key)
            item = response['Item']
            print(item)
        
        except ClientError as e:
            logging.error(e)
            return False
        return True
            
    ############################################################################
    #   retrieve all items from Dynamo DB table
    ############################################################################            
    def get_items_A_to_Z(self,region, table_name):
        try:
            dynamodb_resource = boto3.resource("dynamodb", region_name=region)
            table = dynamodb_resource.Table(table_name)
            
            response = table.scan(
                TableName=table_name,
                Select='ALL_ATTRIBUTES'
		    )
            
        except ClientError as e:
            logging.error(e)
        
        return response['Items']
        
 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    COGNITO CLASS USED FOR INTERACTING WITH COGNITO
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Cognito:
    ############################################################################ 
    #   List all the users on Cognito
    ############################################################################ 
    def list_users(self,args):
        client = boto3.client('cognito-idp', region_name=args['region'])
    
        response = client.list_users(
            UserPoolId=args['UserPoolId'],
            AttributesToGet=[
                'email',
            ],
        )

        return(response)
        
    ############################################################################   
    #   CREATE a new user on Cognito    
    ############################################################################ 
    def sign_up_user(self,args):
        client = boto3.client('cognito-idp', region_name=args['region'])
        
        #args = {'email':email,'password': password,'region':region,'cognitoClientID':cognitoClientID}
        
        response = client.sign_up(
            ClientId=args['cognitoClientID'],
            Username=args['email'],
            Password=args['password'],
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': args['email']
                },
            ],

        )
        return(response)
        
    ############################################################################ 
    #   CONFIRM A USER ON COGNITO
    ############################################################################ 
    def confirm_user(self,region):
        client = boto3.client('cognito-idp', region_name=region)
        
        response = client.admin_confirm_sign_up(
            UserPoolId='us-east-1_412rcjhr9',
            Username='luhvenechenique@gmail.com',
        )