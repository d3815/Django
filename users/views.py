from django.shortcuts import render

from .forms import UserForm
from bboard.models import Bb, Rubric


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
