from django import forms
from django.core.exceptions import ValidationError

from .models import KitchenUser, Profile


class CustomPasswordValidator:
    def __call__(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isalpha() for char in value):
            raise ValidationError("Password must contain at least one letter.")


    def get_help_text(self):
        return "Your password must be at least 8 characters long and contain at least one letter."


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, validators=[CustomPasswordValidator()])
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm Password'
    )

    class Meta:
        model = KitchenUser
        fields = ['email', 'password', 'confirm_password']  # Add more fields as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].help_text = None
        self.fields['password'].help_text = 'Your password must contain at least 8 characters. Your password can’t be entirely numeric.'
        self.fields['confirm_password'].help_text = None
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please try again.")


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'cooking_description', 'image']