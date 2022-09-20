from core.views import ProductView, HeightView, SortView,CommentView
from django.urls import path

urlpatterns = [
    path('<int:pk>/', ProductView.as_view({'get': 'retrieve'})),
    path('', ProductView.as_view({'get': 'list'})),
    path('Height/', HeightView.as_view({'get': 'list'})),
    path('Sort/', SortView.as_view({'get': 'list'})),
    path('<int:product_pk>/product/comment', CommentView.as_view({'post': 'create'
                                                                  })),

]
