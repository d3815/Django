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


'''class ArticleForm(ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }'''