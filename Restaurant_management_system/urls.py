from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL (homepage)
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls', namespace='shop')),
    path('shop/<int:table_number>/', views.table_detail, name='table_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)