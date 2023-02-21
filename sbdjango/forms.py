from django import forms


class UserReg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()

class Userlogin(forms.Form)
    username = forms.CharField(max_length=100)
    user_password = forms.CharField()