from django.contrib import admin

# Register your models here.
from .models import Bb, Rubric, Comment


class BbAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'price', 'published', 'rubric', 'url')
	list_display_links = ('title', 'content')
	search_fields = ('title', 'content')
	prepopulated_fields = {'url':('title',)}

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email', 'body')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(Comment)