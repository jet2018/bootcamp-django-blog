from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, NumberInput, Textarea

from product.models import Product

class ProductModelForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Product Description',  'rows': 5,
                'cols': 40,}),
            'price': NumberInput({'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError('Name must be 3 characters long or more')
        return name

