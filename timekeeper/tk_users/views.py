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
    return render(request,'admin_user.html')
    
def admin_cognito_users(request):
    cognito_users = list ()
    
    # retrieve the list of users 
    region = 'us-east-1'
    client = boto3.client('cognito-idp', region_name=region)
    
    users_resp = client.list_users(
        UserPoolId='us-east-1_412rcjhr9',
        AttributesToGet=[
            'email',
        ],
    )
    
    #   SEE THIS EXAMPLE
    #   https://gist.github.com/jpbarto/c484c923c365b3e391b8eb5029cbaebc
    
    # iterate over the returned users and extract username and email
    for user in users_resp['Users']:
        user_record = {'username': user['Username'], 'email': None}
        
        for attr in user['Attributes']:
            if attr['Name'] == 'email':
                user_record['email'] = attr['Value']
                
        cognito_users.append(user_record)
                
    
    args = {'cognito_users': cognito_users}
    #print(response)
 
    
    #return HttpResponse(cognito_users)
    return render(request,'admin_cognito_users.html',args)