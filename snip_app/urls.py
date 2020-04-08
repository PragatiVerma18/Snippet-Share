from django.conf.urls import url
from snip_app import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^p/(?P<link_c>[-\w]+)/$', views.show_snip, name='show_snips'),
    url(r'^all/$', views.all, name='all'),
    url(r'^search/(?P<link_c>[-\w]+)/$', views.search, name='search'),
    url(r'^edit/(?P<link_c>[-\w]+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<link_c>[-\w]+)/$', views.delete, name='delete'),
]