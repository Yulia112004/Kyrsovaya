from django import forms

from catalog.models import Product, Version

class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_active":
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_disc', 'image', 'category', 'price', 'data_created', 'data_changed']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_product_name(self):
        product_name = self.cleaned_data['product_name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in product_name:
                raise forms.ValidationError(f"Название содержит запрещенное слово: {word}")
        return product_name

    def clean_product_disc(self):
        product_disc = self.cleaned_data['product_disc']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in product_disc:
                raise forms.ValidationError(f"Описание содержит запрещенное слово: {word}")
        return product_disc


class VersionForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ['version_number', 'version_name', 'is_active']

