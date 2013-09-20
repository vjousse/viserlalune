import pprint
from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage

page_fieldsets = deepcopy(PageAdmin.fieldsets)
#page_fieldsets[0][1]["fields"] += ("short_description",)
page_fieldsets[0][1]["fields"].insert(-2, "short_description")

class MyPageAdmin(PageAdmin):
    fieldsets = page_fieldsets

#admin.site.unregister(RichTextPage)
#pprint.pprint(MyPageAdmin.fieldsets)
#admin.site.register(RichTextPage, MyPageAdmin)
