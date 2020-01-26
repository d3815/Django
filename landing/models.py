from django.db import models

# Create your models here.
class User(models.Model):
	"""docstring for User"""
	email = models.EmailField()
	password = models.CharField(max_length=20) #заменить филд