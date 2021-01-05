from django.conf.urls import url
from django.urls import path
from snip_app import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^p/(?P<link_c>[-\w]+)/$', views.show_snip, name='show_snips'),
    url(r'^all/$', views.all, name='all'),
    url(r'^search/(?P<link_c>[-\w]+)/$', views.search, name='search'),
    path('delete_snippet/<str:snippet_id>',views.delete_snippet,name='delete'),
]