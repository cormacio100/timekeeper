from django import forms

class AddCompanyForm(forms.Form):
    name = forms.CharField(label='Company Name', max_length=100)
    eircode = forms.CharField(label='Eircode', max_length=20)