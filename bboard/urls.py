from django.urls import path 
from .views import CurrentRubricListView, BbCreateProductView, ProductListView, ProductDetailView

urlpatterns = [
	path('rubric/<int:rubric_id>', CurrentRubricListView.as_view(), name='by_rubric'),
	path('', ProductListView.as_view(), name=''),
	path('add/', BbCreateProductView.as_view(), name='add'),
	path('<int:pk>', ProductDetailView.as_view(), name='productDetail'),
]