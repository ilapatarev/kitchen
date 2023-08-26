from django import forms
from .models import KitchenUser, Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm Password'
    )

    class Meta:
        model = KitchenUser
        fields = ['email', 'password', 'confirm_password']  # Add more fields as needed

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