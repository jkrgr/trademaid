from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput(),}
        exclude = ('date_joined', 'last_login')