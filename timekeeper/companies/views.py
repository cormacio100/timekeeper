from django.shortcuts import render

# Create your views here.
def index(request):
    '''The home page for Learning Long'''
    return render(request,'companies/index.html')

def adminUser(request):
    '''The home page for Learning Long'''
    return render(request,'companies/adminUser.html')
    
def generalUser(request):
    '''The home page for Learning Long'''
    return render(request,'companies/generalUser.html')