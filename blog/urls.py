from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, blog_is_publication
# from catalog.views import ProductListView, ContactsPageView, PriductDetailView

app_name = BlogConfig.name

urlpatterns = [
    path("create/", BlogCreateView.as_view(), name="create"),
    path("", BlogListView.as_view(), name="list"),
    path("view/<int:pk>/", BlogDetailView.as_view(), name="view"),
    path("update/<int:pk>/", BlogUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", BlogDeleteView.as_view(), name="delete"),
    path("activity/<int:pk>/", blog_is_publication, name="blog_is_publication")
]
