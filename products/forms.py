from django import forms

class ProductCreateForm(forms.Form):
    image = forms.ImageField(required=False)
    name = forms.CharField(max_length=20)
    quantity = forms.FloatField()
    description = forms.CharField(max_length=100, min_length=10)

class CategoryCreateForm(forms.Form):
    title = forms.CharField(min_length=20)
