from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'nickname',
                                      'class': 'input',
                                      'placeholder': 'Username'}),
        label=''
    )
    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'input',
                                          'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class': 'input',
                                          'placeholder': 'Password'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'nickname',
                                      'class': 'input',
                                      'placeholder': 'Username'}),
        label=''
    )
    password = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'class': 'input',
                                          'placeholder': 'Password'}),
    )

    class Meta:
        model = User
        fields = ('username', 'password')
