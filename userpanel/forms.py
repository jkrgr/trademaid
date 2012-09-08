from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        widgets = {'password':forms.PasswordInput(),}
        exclude = ('date_joined', 'last_login')
		

class RegisterForm(UserCreationForm):
	email = forms.EmailField(label = "E-mail address")
	"""phonenumber = forms.TextField(label = "Mobile phone number")"""
    