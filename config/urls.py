from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', views.contacts, name='contacts'),
    path('', include('catalog.urls', namespace='catalog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





