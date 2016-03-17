# Author Luis Manuel Gutierrez http://luismanu.com
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm

from .models import Profile




class CustomUsernameField(forms.CharField):
    def to_python(self, value):
        return value.lower()


class UserCreateForm(UserCreationForm):
    username = CustomUsernameField()

    def clean_email(self):
        error_messages = {
            'duplicate_email': 'A user with this email address already exists'
        }

        email = self.cleaned_data["email"]
       
        try:
            User._default_manager.get(email=email)
            raise forms.ValidationError(error_messages['duplicate_email'], code='duplicate_email')
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        user_profile = Profile(user=user)

        if commit:
            user.save()
            user_profile.save()
        return user, user_profile

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'})
        }