from django import forms

class AddCognitoUserForm(forms.Form):
    email = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
