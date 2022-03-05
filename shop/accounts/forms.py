from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', max_length=100)
    password2 = forms.CharField(label='Confirm Password', max_length=100)

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['passowrd2']:
            raise ValidationError("Passwords don't match ")

        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.changed_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(
        help_text="You can change your password <a href='../password/'>here</a>")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name',
                  'password', 'last_login')

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'password')

        widgets = {
            "password": forms.PasswordInput()
        }