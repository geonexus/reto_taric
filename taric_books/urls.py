__author__ = 'Geon'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /taric_books/
    url(r'^$', views.index, name='index'),
    # ex: /taric_books/results/
    url(r'^results/$', views.results, name='results'),
    # ex: /taric_books/5555555/
    url(r'^(?P<isbn>[-\w]+)/$', views.detail, name='detail'),
    # ex: /taric_books/author/John
    url(r'^author/(?P<author>[-\w]+)/$', views.author, name='author'),
    # ex: /taric_books/author/John/page/1
    url(r'^author/(?P<author>[-\w]+)/page/(?P<page>[-\w]+)/$', views.author, name='author'),
]