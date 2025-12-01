from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError('Invalid username or password')
            elif not user.is_active:
                raise ValidationError('This account is inactive')

        return cleaned_data