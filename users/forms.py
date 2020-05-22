from django.forms import ModelForm
from django import forms
from .models import User


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('email', 'password')
		# exclude = () поля которые нужно исключить (противоположность от филдс)


class LoginForm(ModelForm):
	username = forms.CharField(max_length = 100)
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('email', 'password')
