from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput)

    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
