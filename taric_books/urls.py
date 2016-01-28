__author__ = 'Geon'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /taric_books/
    url(r'^$', views.index, name='index'),
    # ex: /taric_books/results/
    url(r'^results/$', views.results, name='results'),
    # ex: /taric_books/author/
    url(r'^author/$', views.author, name='author'),
        # ex: /taric_books/author_page/author
    url(r'^author_page/(?P<author>[-\w]+)/$', views.author_page, name='author_page'),
    # ex: /taric_books/isbn/
    url(r'^(?P<isbn>[-\w]+)/$', views.isbn, name='isbn'),


]