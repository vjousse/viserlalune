from markdown import markdown

def codehilite(content):
    """
    Renders content using markdown with the codehilite extension.
    """
    return markdown(content, ['codehilite',])


def plain(content):
    """
    Renders content using markdown (no extensions).
    Explicit is better than implicit....
    """
    return markdown(content)


