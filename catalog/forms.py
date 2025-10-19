from django import forms
from catalog.models import Product
import json

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            self.add_error('price', 'Цена не может быть отрицательной')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        with open("catalog/forbidden_words.json", encoding="utf-8") as f:
            words = json.load(f)

        if name and name.lower() in words['forbidden_words']:
            self.add_error('name', 'Название содержит недопустимые слова')
        if description and description.lower() in words['forbidden_words']:
            self.add_error('description', 'Описание содержит недопустимые слова')
