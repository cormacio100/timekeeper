from django.http import Http404
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

# Welcome page for teh application
def index(request):
    return render(request,'index.html')

#   GENERAL User Landing page
def general_user(request):
    return render(request,'general_user.html')
    
#   ADMIN User Landing page
def admin_user(request):
    args = {'heading' : 'Admin Task'}
    return render(request,'admin_user.html',args)
   
#   LISTING PAGE FOR COGNITO USERS
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
            response = cognitoClient.sign_up_user(args)
            
            #   reload the UPDATED list of cognito users
            return redirect(reverse('tk_users:admin_cognito_user_list'))
    else:  
        form = AddCognitoUserForm()
        
        args = {'heading' : 'Add User', 'form': form}
        args.update(csrf(request))

        return render(request,'cognito_user/admin_cognito_user_add.html',args)

def admin_cognito_user_error(request):
    args = {'heading' : 'Upload Error'}
    return render(request,'cognito_user/admin_cognito_user_error.html',args)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    COGNITO CLASS USED FOR INTERACTING WITH COGNITO
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Cognito:
    
    #   List all the users on Cognito
    def list_users(self,args):
        client = boto3.client('cognito-idp', region_name=args['region'])
    
        response = client.list_users(
            UserPoolId=args['UserPoolId'],
            AttributesToGet=[
                'email',
            ],
        )

        return(response)
        
        
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