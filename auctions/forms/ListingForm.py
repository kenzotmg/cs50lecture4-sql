from django import forms
from django.core.validators import MinValueValidator

class ListingForm(forms.Form):
    title = forms.CharField(label="Title")
    startingBid = forms.IntegerField(validators=[MinValueValidator(1.0)])
    picture = forms.CharField(label="Picture URL(Optional)",required=False)
    description = forms.CharField(widget=forms.Textarea)