from django.conf.urls import url,include
from snip_app import views
from .ApiViewset import SnippetViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('snips', SnippetViewset, basename = 'snips')

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^p/(?P<link_c>[-\w]+)/$', views.show_snip, name='show_snips'),
    url(r'^all/$', views.all, name='all'),
    url(r'^search/(?P<link_c>[-\w]+)/$', views.search, name='search'),
    url(r'^getSnipAPI/',include(router.urls),name ='getSnipAPI'),# this URL belong to API testing
]