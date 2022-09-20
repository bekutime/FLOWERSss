from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from auth_app.views import RegisterView,LoginView
from core.views import ProductView, SortView, HeightView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Product/', include('core.urls')),
    path('auth/', include('rest_framework.urls')),
    path('auth-employe/', include('auth_app.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
