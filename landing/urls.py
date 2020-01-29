from django.urls import path 
from .views import landing, create_user

urlpatterns = [
	path('', landing, name='landing'),
	path('landing/create_user', create_user, name='create_user'),
] 