from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        for product in context_data["product_list"]:
            active_version = Version.objects.filter(product=product, version_sign=True)
            if active_version:
                product.active_version = active_version.last().version_name
            else:
                product.active_version = "Отсутствует"
        return context_data


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


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

    # def form_valid(self, form):
    #     product = form.save(commit=False)
    #     product.owner = self.request.user
    #     product.save()
    #     return redirect('catalog:products_list', product.pk)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (
            user.has_perm("products.can_change_description")
            and user.has_perm("products.can_change_category")
            and user.has_perm("products.can_cancel__is_published")
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy("catalog:products_list")


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
