from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        # fields = ('name', 'description', 'category', 'price',)





