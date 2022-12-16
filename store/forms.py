from django import forms
from .models import Product, OrderItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['order_quantity']

    