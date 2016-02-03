__author__ = 'Geon'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /taric_books/
    url(r'^$', views.index, name='index'),
    # ex: /taric_books/taric/
    url(r'^taric/$', views.taric, name='taric'),
    # ex: /taric_books/github/
    url(r'^github/$', views.github, name='github'),
    # ex: /taric_books/about/
    url(r'^about/$', views.about, name='about'),
    # ex: /taric_books/search/
    url(r'^search/$', views.search, name='search'),
    # ex: /taric_books/search_page/search
    url(r'^search_page/(?P<search>[-\w]+)/(?P<search_type>[-\w]+)/$', views.search_page, name='search_page'),
    # ex: /taric_books/isbn/
    url(r'^(?P<value>[-\w]+)/$', views.isbn, name='isbn'),

]
