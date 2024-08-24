from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsPageView, ProductDetailView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name


urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path('create/', ProductCreateView.as_view(), name="products_create"),
    path('update/<int:pk>', ProductUpdateView.as_view(), name="products_update")
]
