from django.db import models


class Bb(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	published = models.DateTimeField(auto_now_add=True, db_index=True)
	rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, 
								verbose_name='Рубрики')
	product = models.ForeignKey('Comment', null=True, on_delete=models.CASCADE)
	#image = models.ImageField(upload_to='image')


	def __str__(self):
		return self.title


	class Meta:
		verbose_name_plural = 'Объявления'
		verbose_name = 'Объявление'
		ordering = ['-published'] #по умолчанию сортировать результаты по полю 
								#publish в убывающем порядке при запросе к базе данных. 
								#Мы указываем убывающий порядок с помощью отрицательного префикса.


class Rubric(models.Model):
	name = models.CharField(max_length=20, db_index=True, verbose_name='Название')


	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = 'Рубрики'
		verbose_name = 'Рубрики'
		ordering = ['name']


class Comment(models.Model):
	post = models.ForeignKey(Bb, related_name='comments', on_delete=models.CASCADE)
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)
		verbose_name_plural = 'Комментарии'
		verbose_name = 'Комментарий'
		
	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.post)
