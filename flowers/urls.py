from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from auth_app.views import RegisterView,LoginView
from core import views
from core.views import ProductView, SortView, HeightView

# router = routers.DefaultRouter()
# router.register('image', views.ImageView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Product/', include('core.urls')),
    path('auth/', include('rest_framework.urls')),
    path('auth-employe/', include('auth_app.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls
