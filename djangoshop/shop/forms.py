from django import forms
from django.forms import CharField,EmailField,PasswordInput
class LoginForm(forms.Form):
    username=CharField(max_length=555)
    password=CharField(widget=PasswordInput(),max_length=555)

class RegisterForm(forms.Form):
    name=CharField(max_length=30)
    email=EmailField(max_length=100)
    password=CharField(widget=PasswordInput(),max_length=555)
    Repeat_password=CharField(widget=PasswordInput(),max_length=555)