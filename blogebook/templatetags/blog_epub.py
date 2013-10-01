from django import template
from ebooklib import epub

register = template.Library()

def posts_epub_link(posts):

    book = epub.EpubBook()

    # add metadata
    book.set_title('Articles de Vincent Jousse')
    book.set_language('fr')

    book.add_author('Vincent Jousse')


    for post in posts:
        print post.title
        c1 = epub.EpubHtml(title=post.title, file_name='%s.xhtml' % post.slug, lang='fr')
        c1.content=u'<html><head></head><body><h1>Introduction</h1><p>Voici une belle introduction.</p></body></html>'

    book.add_item(c1)

    # add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # define css style
    style = '''
@namespace epub "http://www.idpf.org/2007/ops";

body {
    font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
}

h2 {
     text-align: left;
     text-transform: uppercase;
     font-weight: 200;     
}

ol {
        list-style-type: none;
}

ol > li:first-child {
        margin-top: 0.3em;
}


nav[epub|type~='toc'] > ol > li > ol  {
    list-style-type:square;
}


nav[epub|type~='toc'] > ol > li > ol > li {
        margin-top: 0.3em;
}

'''

    # add css file
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    # create spine
    book.spine = ['nav', c1 ]

    # create epub file
    epub.write_epub('test.epub', book, {})


    return "/test.epub"

register.simple_tag(posts_epub_link)
