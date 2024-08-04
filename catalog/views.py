from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products_detail.html", context)


def base(request):
    return render(request, "base.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(
            f"{name} написал следующее сообщение: {message}, контактный телефон: {phone}"
        )
    return render(request, "contacts.html")
