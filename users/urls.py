from django.contrib.auth import views
from django.urls import path, include
from django.conf.urls import url
#from login_auth import views as login_views
from django.conf import settings

from .views import create_user, profile, login


urlpatterns = [
	#path('login/', views.LoginView.as_view(), name='login'),
	#path('sign_in/', sign_in, name='sign_in'),
	path('login/', login, name='login'),
	#path('logout/', logout, name='logout'),
	path('create_user/', create_user, name='create_user'),
	path('profile/', profile, name='profile'),
]