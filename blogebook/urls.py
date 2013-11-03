from django.conf.urls import patterns, url

from blogebook import views

urlpatterns = patterns('',
    url(r'^download/epub/slug/(?P<aSlug>.*)$', views.post_epub_download, name='post_epub_download'),
    url(r'^download/epub/(?P<category>.*)$', views.posts_epub_download, name='posts_epub_download'),
    url(r'^download/epub$', views.posts_epub_download, name='posts_epub_download')
)
