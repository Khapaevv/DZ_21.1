from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product

class PriductDetailView(DetailView):
    model = Product

def base(request):
    return render(request, "base.html")

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

