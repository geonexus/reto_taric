__author__ = 'Geon'
from django import forms
from reto_taric.constants import SEARCH_TYPES


class SearchFormType(forms.Form):
    search_type = forms.ChoiceField(choices=SEARCH_TYPES,
                                widget=forms.Select, label="Search filter")


class SearchFormValue(forms.Form):
    search_value = forms.CharField(max_length=100, required=True, label="")


class PageForm(forms.Form):
    page_value = forms.IntegerField(label='Go Page')
