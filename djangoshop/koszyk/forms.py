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

    def clean_Address(self):
        data=self.cleaned_data.get('Address')
        if len(data) <= 5:
            raise forms.ValidationError('Za krótki adres')
        return data
    def clean_Tel(self):
        data=self.cleaned_data.get('Tel')
        if len(str(data)) < 9:
            raise forms.ValidationError('Za krótki numer telefonu')
        return data