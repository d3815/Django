from django.shortcuts import render

from .forms import UserForm
# Create your views here.

def landing(request):
	form = UserForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		data = form.cleaned_data
		print(data)

	return render(request, 'landing/landing.html', locals())


def create_user(request):
	form = UserForm(request.POST or None)
	return render(request, 'landing/create_user.html', locals())
