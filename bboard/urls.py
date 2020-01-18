from django.urls import path 
from .views import index, by_rubric, BbCreateView, by_lot

urlpatterns = [
	path('rubric/<int:rubric_id>', by_rubric, name='by_rubric'),
	path('', index, name='index'), 
	path('add/', BbCreateView.as_view(), name='add'),
	path('lot/<int:lot_id>', by_lot, name='by_lot'), 
]