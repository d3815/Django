from django.urls import path 
from .views import CurrentRubricListView, BbCreateProductView, ProductListView, by_product#, CommentAddReview

urlpatterns = [
	path('rubric/<int:rubric_id>', CurrentRubricListView.as_view(), name='by_rubric'),
	path('', ProductListView.as_view(), name='index'),
	path('add/', BbCreateProductView.as_view(), name='add'),
	path('product/<int:product_id>-<slug:url>', by_product, name='by_product'),
	#path('review/<int:pk>', CommentAddReview, name='add_review'),
]