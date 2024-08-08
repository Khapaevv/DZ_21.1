from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsPageView, PriductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("products/<int:pk>/", PriductDetailView.as_view(), name="products_detail"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
]
