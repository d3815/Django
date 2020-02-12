from django.forms import ModelForm

from .models import Bb, Comment

class BbForm(ModelForm):
	class Meta:
		model = Bb
		fields = ('title', 'content', 'price', 'rubric')


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')