from django import forms

class EssayForm(forms.Form):
    title = forms.CharField(max_length=100)
    essay = forms.CharField(widget=forms.Textarea)
