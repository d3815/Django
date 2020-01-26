from django.shortcuts import render

from .forms import UserForm
# Create your views here.

def landing(request):
	form = UserForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		print(request.POST)
		print (form.cleaned_data)

	return render(request, 'landing/landing.html', locals())
