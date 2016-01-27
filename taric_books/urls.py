__author__ = 'Geon'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /books/
    url(r'^$', views.index, name='index'),
    # ex: /books/results/
    url(r'^results/$', views.results, name='results'),
    # ex: /books/5/
    url(r'^(?P<isbn>[-\w]+)/$', views.detail, name='detail'),
    # ex: /books/5/vote/
    url(r'^(?P<isbn>[-\w]+)/vote/$', views.vote, name='vote'),
]