from django.conf.urls import url

from . import views

PROJECT = r'(?P<project>[^/]+)/'

urlpatterns = [
    url(
        r'^$',
        views.crawl,
        name='crawl',
    ),
    ## 0222_bikemap_crawaler
    url(
        r'^crawl/$',
        views.crawl,
        name='crawl1',
    ),

]


