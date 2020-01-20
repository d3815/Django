from django.db import models

# Create your models here.
class Bb(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	published = models.DateTimeField(auto_now_add=True, db_index=True)
	rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, 
								verbose_name='Рубрики')
	#image = models.ImageField(blank=True, upload_to='images/blog/%Y/%m/%d', help_text='150x150px', verbose_name='Ссылка картинки')


	def __str__(self):
		return self.title


	class Meta:
		verbose_name_plural = 'Объявления'
		verbose_name = 'Объявление'
		ordering = ['title']


class Rubric(models.Model):
	name = models.CharField(max_length=20, db_index=True, verbose_name='Название')


	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = 'Рубрики'
		verbose_name = 'Рубрики'
		ordering = ['name']