# Create your views here.

from sitecontent.models import PostsRSSRichtextFilters, PostsAtomRichtextFilters

def blog_post_feed_richtext_filters(request, format, **kwargs):
    """
    Blog posts feeds - maps format to the correct feed view.
    """
    try:
        return {"rss": PostsRSSRichtextFilters, "atom": PostsAtomRichtextFilters}[format](**kwargs)(request)
    except KeyError:
        raise Http404()
