from django.forms import ModelForm
from django import forms

from .models import Bb, Comment


class BbForm(ModelForm):
	# title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}))
	class Meta:
		model = Bb
		fields = ('title', 'content', 'price', 'rubric', 'image')


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')

