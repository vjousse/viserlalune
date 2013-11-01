from django.conf.urls import patterns, url

from bestof import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='bestof_index')
)
