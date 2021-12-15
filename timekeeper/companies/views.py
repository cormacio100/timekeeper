from django.shortcuts import render
from .forms import AddCompanyForm

# Create your views here.

#def index(request):
 #   '''The home page for Learning Long'''
  #  return render(request,'companies/index.html')

def admin_company_list(request):
    args = {'heading':'Client Listing'}
    return render(request,'companies/admin_company_list.html',args)


def admin_company_add(request):
    form = AddCompanyForm()
    
    args = {'heading' : 'Add Client', 'form': form}
    return render(request,'companies/admin_company_add.html',args)