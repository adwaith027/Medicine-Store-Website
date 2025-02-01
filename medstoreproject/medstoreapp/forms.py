from django import forms
from .models import storeModel

class storeForm(forms.ModelForm):
    class Meta:
        model=storeModel
        fields=['name','company','price','quantity','expiry','picture']
        
    labels={'name':'Medicine Name','company':'Manufacturer','price':'Price','quantity':'Quantity','expiry':'Expiry Date','picture':'Upload Picture'}

    widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Medicine Name'}),
            'company':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Manufacturer Name'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Price'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Quantity'}),
            'expiry':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Expiry Date'}),
            'picture':forms.FileInput(attrs={'class':'form-control'})
        }