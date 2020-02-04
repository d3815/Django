from django.shortcuts import render

from .forms import UserForm


def sign_in(request):
	form = UserForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		data = form.cleaned_data
		print(data)

	return render(request, 'users/sign_in.html', locals())


def create_user(request):
	form = UserForm(request.POST or None)
	return render(request, 'users/create_user.html', locals())
