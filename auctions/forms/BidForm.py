from django import forms
from django.core.exceptions import ValidationError

class BidForm(forms.Form):
    bid = forms.IntegerField()

    def __init__(self,minvalue,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def clean(self):
        if self.bid <= minvalue:
            raise ValidationError('Bid is equal or less than current bid')