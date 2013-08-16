from django import forms

class WmdWidget(forms.Textarea):
    """
    Enables wmd editor for this textarea and any
    others with a 'wmd-widget' class assigned
    """

    def __init__(self, *args, **kwargs):
        super(WmdWidget, self).__init__(*args, **kwargs)
        self.attrs['class'] = 'wmd-widget wmd-panel'

    class Media:
        css = {'all': ('mdown/wmd/wmd.css',)}
        js = ('mdown/jquery-1.4.4.min.js',
              'mdown/wmd/jquery.wmd.min.js',)


class PlainWidget(forms.Textarea):
    """
    A regular Textarea widget that is compatible with mezzanine richtext.
    """

    class Media:
        pass
