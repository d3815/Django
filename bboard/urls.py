from django.urls import path 
from .views import index, by_rubric, BbCreateProductView, by_product

urlpatterns = [
	path('rubric/<int:rubric_id>', by_rubric, name='by_rubric'),
	path('', index, name='index'), 
	path('add/', BbCreateProductView.as_view(), name='add'),
	path('product/<int:product_id>', by_product, name='by_product'), 
] 