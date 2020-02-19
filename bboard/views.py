from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from .forms import BbForm, CommentForm
from .models import Bb, Rubric, Comment


'''
bbs = Bb.objects.all()
rubrics = Rubric.objects.all()
comments = Comment.objects.all()
context = {
			'bbs': bbs,
			'rubrics': rubrics,
			'comments': comments
		}'''

class ProductListView(View):
	'''Список товаров'''
	def get(self, request):
		bbs = Bb.objects.all()
		rubrics = Rubric.objects.all()
		comments = Comment.objects.all()
		paginator = Paginator(bbs, 4)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context = {
			'bbs': bbs,
			'rubrics': rubrics,
			'page_obj': page_obj,
			'comments': comments
		}
		return render(request, 'bboard/index.html', context)

	# разбить по Х объявлений на одной странице
	# https://pocoz.gitbooks.io/django-v-primerah/dobavlenie-paginacii.html

class CurrentRubricListView(View):
	'''Список категорий'''
	def get(self, request, rubric_id):
		bbs = Bb.objects.filter(rubric=rubric_id)
		rubrics = Rubric.objects.all()
		current_rubric = Rubric.objects.get(pk=rubric_id)
		context = {
			'bbs': bbs,
			'rubrics': rubrics,
			'current_rubric': current_rubric
		}
		return render(request, 'bboard/by_rubric.html', context)


class ProductDetailView(View):
	'''Полное описание определенного товара'''
	def get(self, request, pk):
		products_list = Bb.objects.all()
		current_product = Bb.objects.get(id=pk)
		rubrics = Rubric.objects.all()
		comments = Comment.objects.filter(post=pk)
		#latest_question_list = Question.objects.order_by('-pub_date')[:5]
		if request.method == 'POST':
			form = CommentForm(request.POST)
			if form.is_valid():
				print(form.cleaned_data)
		else:
			form = CommentForm()

		context = {
			'products_list' : products_list,
			'current_product': current_product,
			'rubrics': rubrics,
			'comments' : comments,
			'form' : form
		}
		return render(request, 'bboard/by_product.html', context)


class BbCreateProductView(CreateView):
	template_name = 'bboard/create_product.html'
	form_class = BbForm
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rubrics'] = Rubric.objects.all()
		context['bbs'] = Bb.objects.all()
		return context