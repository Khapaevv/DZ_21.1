from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import Product_list, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', Product_list),
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
