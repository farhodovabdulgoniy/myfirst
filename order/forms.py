from django import forms
from order.models import *


class OrderForm(forms.ModelForm):
    
    class Meta:

        model = Order 
        fields = ('first_name','last_name','address','phone','city','country')