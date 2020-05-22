from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# from django.contrib import auth


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth

from .forms import LoginForm
from bboard.models import Rubric, Bb

'''def sign_in(request):
	form = UserForm(request.POST or None)
	#bbs = Bb.objects.all()
	rubrics = Rubric.objects.all()
	if request.method == "POST" and form.is_valid():
		data = form.cleaned_data
		print(data)

	context = {'rubrics': rubrics}
	return render(request, 'users/sign_in.html', locals())'''

'''def sign_in(request):
    rubrics = Rubric.objects.all()
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
    context = {'rubrics': rubrics, 'form': form}
    return render(request, 'users/sign_in.html', context)


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(‘/’) '''


def login(request):
    rubrics = Rubric.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(user)
        else:
            pass
    return render(request, 'users/sign_in.html', locals())


def create_user(request):
    # form = UserForm(request.POST or None)
    rubrics = Rubric.objects.all()
    context = {'rubrics': rubrics}
    return render(request, 'users/create_user.html', locals())


def profile(request):
    rubrics = Rubric.objects.all()
    context = {'rubrics': rubrics}
    return render(request, 'users/profile.html', locals())
