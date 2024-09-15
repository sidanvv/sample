from django import forms 
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','phone']
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'email':forms.EmailInput(attrs={'placeholder':"enter your email"}),
            'phone':forms.NumberInput(attrs={"placeholder":"enter your phone number"})
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        