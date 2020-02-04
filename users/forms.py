from django.forms import ModelForm

from .models import User

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('email', 'password')
		#exclude = () поля которые нужно исключить (противоположность от филдс)