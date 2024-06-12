from django import forms

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

class loginform(forms.Form):
    email = forms.CharField(max_length=50) 
    password = forms.CharField(widget=forms.PasswordInput()) 