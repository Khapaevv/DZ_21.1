from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product

# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "products_list.html", context)


class ProductDetailView(DetailView):
    model = Product

# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "products_detail.html", context)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


class BasePageView(TemplateView):
    template_name = "catalog/base.html"

# def base(request):
#     return render(request, "base.html")

class ContactsPageView(TemplateView):
    template_name = "catalog/contacts.html"


    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")

            print(
                f"{name} написал следующее сообщение: {message}, контактный телефон: {phone}"
            )
        return render(request, "catalog/contacts.html")

# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#
#         print(
#             f"{name} написал следующее сообщение: {message}, контактный телефон: {phone}"
#         )
#     return render(request, "contacts.html")

