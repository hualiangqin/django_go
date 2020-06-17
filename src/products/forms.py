from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    # overwrite the fields in models.py
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "my_class",
                "id": "my_id",
                "rows": 20,
                "cols": 50
            }
        )
    )
    price = forms.DecimalField(initial=998.98)
    email = forms.EmailField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "amc" not in title:
            raise forms.ValidationError("This is not a valid title")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if "edu" not in email:
            raise forms.ValidationError("This is not a valid email")
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class" : "my_class",
                "id": "my_id",
                "rows": 20,
                "cols": 50
            }
        )
    )
    price = forms.DecimalField(initial=998.98)
