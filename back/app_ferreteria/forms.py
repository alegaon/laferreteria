# En forms.py de tu aplicación

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    date_of_birth = forms.DateField(required=False)
    country = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User  # Cambia 'Profile' a 'User'
        fields = ['username', 'password1', 'password2', 'date_of_birth', 'country']
