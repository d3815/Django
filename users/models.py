from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=50)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    profile_pic = models.ImageField(upload_to='Accounts/Profile', blank=True)

    def __str__(self):
        return self.user.username


class User(models.Model):
    """docstring for User"""
    email = models.EmailField()
    password = models.CharField(max_length=20)  # заменить филд

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['email']


'''class LoginForm(models.Model):
	"""docstring for User"""
	email = models.EmailField()
	password = models.CharField(max_length=20) #заменить филд

	def __str__(self):
		return self.email

	class Meta:
		verbose_name_plural = 'Пользователи'
		verbose_name = 'Пользователь'
		ordering = ['email']  '''
