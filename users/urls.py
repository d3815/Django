from django.urls import path 
from .views import sign_in, create_user

urlpatterns = [
	path('sign_in/', sign_in, name='sign_in'),
	path('create_user/', create_user, name='create_user'),
] 