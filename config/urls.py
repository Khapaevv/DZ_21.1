from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', views.contacts, name='contacts'),
    path('', include('catalog.urls', namespace='catalog'))
]
