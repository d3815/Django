from django.urls import path 
from .views import by_rubric, BbCreateProductView, by_product, ProductView

urlpatterns = [
	path('rubric/<int:rubric_id>', by_rubric, name='by_rubric'),
	path('', ProductView.as_view(), name=''),
	path('add/', BbCreateProductView.as_view(), name='add'),
	path('product/<int:product_id>', by_product, name='by_product'), 
] 