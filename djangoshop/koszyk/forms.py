from dataclasses import field
from django import forms
from .models import *
choices=[(i,str(i)) for i in range(1,21)]
class AddProduct(forms.Form):
    quantity=forms.TypedChoiceField(choices=choices,coerce=int)

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
