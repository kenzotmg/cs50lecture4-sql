from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class BidForm(forms.Form):
    bid = forms.IntegerField()

    def __init__(self,*args,**kwargs):
        minValuearg = kwargs.pop('minValue')
        super().__init__(*args,**kwargs)
        bidField = self.fields['bid']
        bidField.validators.append(MinValueValidator(minValuearg+1))
        bidField.initial = minValuearg+1