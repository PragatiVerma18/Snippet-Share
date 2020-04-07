from django.conf.urls import include, url
from fileupload.views import FileCreateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = [

url(r'^$', FileCreateView.as_view(), name='home'),

]