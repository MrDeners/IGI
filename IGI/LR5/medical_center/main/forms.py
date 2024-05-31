import re

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import Review, CustomUser, Service


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('address', 'phone', 'age')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_pattern = r'^\+37529\d{3}\d{2}\d{2}$'
        if not re.match(phone_pattern, phone):
            raise forms.ValidationError('Invalid phone number format. Please use the format +375 (29) XXX-XX-XX.')
        return phone


# TODO: Update Delete and graphic

class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Username ', max_length=30, required=True, widget=forms.TextInput())
    password = forms.CharField(label='Password ', max_length=30, required=True, widget=forms.TextInput())


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'grade', 'text']
        widgets = {
            'name': forms.TextInput(),
            'grade': forms.Select(),
            'text': forms.Textarea(),
        }
