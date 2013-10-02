from django.conf.urls import patterns, url

from sitecontent import views


urlpatterns = patterns('',
    url("^rss/(?P<format>.*)$",
        "sitecontent.views.blog_post_feed_richtext_filters", name="blog_post_feed_richtext_filters"),
)
