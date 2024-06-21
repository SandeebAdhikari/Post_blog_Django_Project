from django import forms
from .models import Scheduler
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SchedulerForm(forms.ModelForm):
    class Meta:
        model = Scheduler
        fields = ['text','photo']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
        }