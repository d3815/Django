from django.urls import path 
from .views import index, by_rubric, BbCreateView, by_lot

urlpatterns = [
	path('<int:rubric_id>', by_rubric, name='by_rubric'),
	path('', index, name='index'), 
	path('add/', BbCreateView.as_view(), name='add'),
	path('by_lot/', by_lot, name='by_lot'), 
]