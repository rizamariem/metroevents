from django import forms
from .models import *



class loginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username',)


class registerForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username',)

