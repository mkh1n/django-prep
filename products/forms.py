from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = (
            'article',
            'name',
            'unit_type',
            'price',
            'supplier',
            'manufacturer',
            'category',
            'discount',
            'stock_quantity',
            'description',
            'photo')
        
        widgets = {
            'article' : forms.TextInput(),
            'name': forms.TextInput(),
            'unit_type': forms.TextInput(),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'supplier': forms.Select(),
            'manufacturer': forms.Select(),
            'category': forms.Select(),
            'discount': forms.NumberInput(attrs = {'step': '0.01'}),
            'stock_quantity': forms.NumberInput(),
            'description': forms.Textarea(attrs = {'rows': 3}),
            'photo': forms.TextInput()
        }
