from django.shortcuts import render
from catalog.models import Product


def Product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'products_list.html', context)

# def home(request):
#     return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'{name} написал следующее сообщение: {message}, контактный телефон: {phone}')
    return render(request, 'contacts.html')
