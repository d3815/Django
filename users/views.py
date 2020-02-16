from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import UserForm, LoginForm
from bboard.models import Rubric #, Bb


def sign_in(request):
	form = UserForm(request.POST or None)
	#bbs = Bb.objects.all()
	rubrics = Rubric.objects.all()
	if request.method == "POST" and form.is_valid():
		data = form.cleaned_data
		print(data)

	context = {'rubrics': rubrics}
	return render(request, 'users/sign_in.html', locals())


def create_user(request):
	form = UserForm(request.POST or None)
	rubrics = Rubric.objects.all()
	context = {'rubrics': rubrics}
	return render(request, 'users/create_user.html', locals())


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})