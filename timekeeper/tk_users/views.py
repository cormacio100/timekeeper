from django.http import Http404
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.template.context_processors import csrf
from .forms import AddCognitoUserForm
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect

import logging
import boto3 

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def general_user(request):
    return render(request,'general_user.html')
    
def admin_user(request):
    args = {'heading' : 'Admin Taks'}
    return render(request,'admin_user.html',args)
    
def admin_cognito_user_list(request):
    cognito_users = list ()
    user_id = 0
    
    # retrieve the list of users 
    region = 'us-east-1'
    #settings.REGION
    client = boto3.client('cognito-idp', region_name=region)
    
    user_list_resp = client.list_users(
        UserPoolId='us-east-1_412rcjhr9',
        AttributesToGet=[
            'email',
        ],
    )
    
    #   SEE THIS EXAMPLE
    #   https://gist.github.com/jpbarto/c484c923c365b3e391b8eb5029cbaebc
    
    
        #    to do
        #   Check Congito user against DYNAMODB
        #   see Flask Project CADynamoFlaskLab app 
    # iterate over the returned users and extract username and email
    # For each record check if they are on the DynamoDB 
    # if yes, proceed. If no then need to add
    # Database is used to link the cognito profile against user details and S3 Buckets
    #   Then 
    for user in user_list_resp['Users']:
        user_record = {'user_id': user_id, 'username': user['Username'], 'email': None}
        
        for attr in user['Attributes']:
            if attr['Name'] == 'email':
                user_record['email'] = attr['Value']
                
        cognito_users.append(user_record)
                
        user_id += 1
    args = {'heading':'Cognito Users','cognito_users': cognito_users}
    #print(response)
 
    
    #return HttpResponse(cognito_users)
    return render(request,'cognito_user/admin_cognito_user_list.html',args)
    
#   FUNCTION Creates A Cognito User based on values entered in a form  
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
            rsponse = cognitoClient.sign_up_user(args)
            
            #   reload the list of cognito users
            #return redirect('tk_users.views.admin_cognito_user_list')
            return redirect(reverse('tk_users:admin_cognito_user_list'))
    else:  
        form = AddCognitoUserForm()
        
        args = {'heading' : 'Add User', 'form': form}
        args.update(csrf(request))

    return render(request,'cognito_user/admin_cognito_user_add.html',args)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    COGNITO CLASS USED FOR INTERACTING WITH COGNITO
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Cognito:
    
    #   List all the users on Cognito
    def list_users(self,region):
        client = boto3.client('cognito-idp', region_name=region)
    
        response = client.list_users(
            UserPoolId='us-east-1_412rcjhr9',
            AttributesToGet=[
                'email',
            ],
        )
        print(response)
        print("----------------------------------------------------")
        print(response['Users'])
        'Users['
        
        
    #   CREATE a new user on Cognito    
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
        
        
    def confirm_user(self,region):
        client = boto3.client('cognito-idp', region_name=region)
        
        response = client.admin_confirm_sign_up(
            UserPoolId='us-east-1_412rcjhr9',
            Username='luhvenechenique@gmail.com',
        )