__author__ = 'Geon'
from django import forms
from reto_taric.constants import SEARCH_TYPES

class SearchForm(forms.Form):

    search_type = forms.ChoiceField(choices=SEARCH_TYPES,
                                widget=forms.Select)
    search_value = forms.CharField(label='Insert Text', max_length=100)

class PageForm(forms.Form):
    page_value = forms.IntegerField(label='Go Page')
