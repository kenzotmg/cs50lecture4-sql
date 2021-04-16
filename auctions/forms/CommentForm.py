from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(label='',widget=forms.Textarea(attrs={'style' : 'width: 100%','rows' : '3','placeholder' : 'Write a comment...'}))