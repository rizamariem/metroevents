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

class regEventForm(forms.ModelForm):
    class Meta:
    	model = Events
    	fields = ('name',)



class promoteForm(forms.ModelForm):
     class Meta:
        model = Organizers
        fields = ('user_id',)

    	

