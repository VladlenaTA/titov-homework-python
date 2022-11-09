from django import forms

from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control mb-2 product-form", "placeholder": "title"}
        )

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ["id"]
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
