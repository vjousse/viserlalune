from django.db import models

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import Atom1Feed
from django.utils.html import strip_tags

from mezzanine.blog.feeds import PostsRSS, PostsAtom
from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.core.templatetags import mezzanine_tags
from mezzanine.conf import settings

# Create your models here.


class PostsRSSRichtextFilters(PostsRSS):
    """
    RSS feed for all blog posts.
    """

    def items(self):
        if not self._public:
            return []
        blog_posts = BlogPost.objects.published().select_related("user")
        if self.tag:
            tag = get_object_or_404(Keyword, slug=self.tag)
            blog_posts = blog_posts.filter(keywords__in=tag.assignments.all())
        if self.category:
            category = get_object_or_404(BlogCategory, slug=self.category)
            blog_posts = blog_posts.filter(categories=category)
        if self.username:
            author = get_object_or_404(User, username=self.username)
            blog_posts = blog_posts.filter(user=author)
        limit = settings.BLOG_RSS_LIMIT
        if limit is not None:
            blog_posts = blog_posts[:settings.BLOG_RSS_LIMIT]

        blog_posts_filter = []

        for post in blog_posts:
           post.content = mezzanine_tags.richtext_filters(post.content)
           blog_posts_filter.append(post)

        return blog_posts_filter



class PostsAtomRichtextFilters(PostsRSSRichtextFilters):
    """
    Atom feed for all blog posts.
    """

    feed_type = Atom1Feed

    def subtitle(self):
        return self.description()

    def link(self):
        return reverse("blog_post_feed", kwargs={"format": "atom"})
