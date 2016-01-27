__author__ = 'Geon'
from django import forms

class SearchForm(forms.Form):
    search_value = forms.CharField(label='Insert Text   ', max_length=100)