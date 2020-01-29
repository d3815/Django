from django.db import models

# Create your models here.
class User(models.Model):
	"""docstring for User"""
	email = models.EmailField()
	password = models.CharField(max_length=20) #заменить филд


	def __str__(self):
		return self.email


	class Meta:
		verbose_name_plural = 'Пользователи'
		verbose_name = 'Пользователь'
		ordering = ['email']