from core import views
from core.views import ProductView, HeightView, SortView, CommentView, CreateView
from django.urls import path
# from rest_framework import routers

#
# router = routers.DefaultRouter()
# router.register('image', views.ImageView)

urlpatterns = [
    path('Product/<int:pk>/', ProductView.as_view({'get': 'retrieve',
                                                   })),
    path('Product/', ProductView.as_view({'get': 'list'})),
    path('Height/', HeightView.as_view({'get': 'list'})),
    path('Sort/', SortView.as_view({'get': 'list'})),
    path('<int:product_pk>/product/comment/', CommentView.as_view({'post': 'create',
                                                                  'get': 'list'})),


    path('ProductCreate/', CreateView.as_view({'post': 'create'})),
]



#    path('<int:product_pk>/product/image/', ImageView.as_view({'post': 'create'}))
#    path('image/', ImageView.as_view({'get': 'list',
#                                    'post': 'create'} )),
