from django import forms
from apps.product.models import product_Models

class edit_Form(forms.ModelForm):
    class Meta:
        model = product_Models
        fields = '__all__'
