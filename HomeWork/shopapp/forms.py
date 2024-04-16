from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']
