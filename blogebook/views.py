from blogebook.ebook import epub

from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404

from mezzanine.blog.models import BlogPost, BlogCategory

def posts_epub_download(request, category=None):
    """
    Construct an ebook using a list of blog posts that are filtered 
    by category.
    """

    blog_posts = BlogPost.objects.published(for_user=request.user)
    if category is not None:
        category = get_object_or_404(BlogCategory, slug=category)
        blog_posts = blog_posts.filter(categories=category)

    content = epub.generate_from_posts(blog_posts)
    response = HttpResponse(content, mimetype='appication/epub+zip')
    if category:
        response['Content-Disposition'] = "attachment; filename=vincent-jousse-articles-%s.epub" % category.slug
    else:
        response['Content-Disposition'] = "attachment; filename=vincent-jousse-articles.epub"


    return response



def post_epub_download(request, aSlug=None):
    """
    Construct an ebook using one blog post.
    """
    blog_posts = BlogPost.objects.published(
                                     for_user=request.user).filter(slug=aSlug).select_related()

    content = epub.generate_from_posts(blog_posts)
    response = HttpResponse(content, mimetype='appication/epub+zip')
    response['Content-Disposition'] = "attachment; filename=vincent-jousse-articles-%s.epub" % aSlug


    return response
