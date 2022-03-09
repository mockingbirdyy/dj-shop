from django import forms
from .models import User, OtpCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'full_name')
        # customize fields: here adding bootstrap 
        widgets = {
            'phone_number': forms.NumberInput(attrs={'class': 'form-control ', 'placeholder': 'Phone number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control  ', 'placeholder': 'Full name'}),
        }
    # Check if passowrds are match
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError("Passwords don't match ")
        return cd['password2']
    # overriding save method
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # Shows a hash of password in admin panel
    password = ReadOnlyPasswordHashField(
        # You can change password in UserCreationForm from ../password/
        help_text="You can change your password <a href='../password/'>here</a>")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name',
                  'password', 'last_login')


class VerifyCodeForm(forms.ModelForm):

    class Meta:
        model = OtpCode
        fields = ('code',)
        widgets = {
            'code': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Code'})
        }