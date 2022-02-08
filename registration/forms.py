from django import forms
from django.core import validators

class UserForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput)

    def clean(self):
        all_clean_data = super().clean()

        p1 = all_clean_data['password']
        p2 = all_clean_data['password2']

        if p1 != p2:
            raise forms.ValidationError('the two password do not match')