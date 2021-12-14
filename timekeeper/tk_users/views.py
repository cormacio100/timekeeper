from django.http import Http404
from django.shortcuts import render
from django.shortcuts import HttpResponse

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
    return render(request,'admin_cognito_user_list.html',args)
    
    
def admin_cognito_user_add(request):
    args = {'heading' : 'Add User'}
    return render(request,'admin_cognito_user_add.html',args)