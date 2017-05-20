# -*- coding: utf-8 -*- 

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
       required= True,
       widget=forms.EmailInput(
           attrs={
                   'class': 'form-control',
                   'placeholder': 'email',
                   'required' : 'true',
            }
       )
    )
    username = forms.RegexField(label="UserName", max_length=30,
               regex=r'^[/w.@+-]+$',
               help_text="Required. 30 chacters or fewer. Letters, digits and " +
                          "@/./+/-/_ only." ,
               error_messages={
                        'invalid' : "This value may contain only letters, numbers and"+
                        "@/./+/-/_ characters."})
    
    class Meta:
       model = User
       fields = ("username", "email", )
   