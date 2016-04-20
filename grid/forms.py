from django import forms

class InputForm(forms.Form):
    grid = forms.CharField(widget=forms.Textarea, required=False)
