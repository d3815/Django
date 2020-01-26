from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import BbForm
from .models import Bb, Rubric


def index(request):
	bbs = Bb.objects.all()
	rubrics = Rubric.objects.all()
	context = {'bbs' : bbs, 'rubrics': rubrics }
	return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
	bbs = Bb.objects.filter(rubric=rubric_id)
	rubrics = Rubric.objects.all()
	current_rubric = Rubric.objects.get(pk=rubric_id)
	context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric }
	return render(request, 'bboard/by_rubric.html', context)


def by_product(request, product_id):
	products_list = Bb.objects.all()
	current_product = Bb.objects.get(pk=product_id)
	rubrics = Rubric.objects.all()
	context = {'products_list' : products_list, 'current_product': current_product, 'rubrics': rubrics}
	return render(request, 'bboard/by_product.html', context)


class BbCreateProductView(CreateView):
	template_name = 'bboard/create_product.html'
	form_class = BbForm
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context