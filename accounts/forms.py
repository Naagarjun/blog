from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import Profile
from django.shortcuts import redirect


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    User._meta.get_field('email')._unique = True

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateDetails(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']


class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = "email not registered, Please check you mail address"
            self.add_error('email', msg)
        return email
