from django.contrib import admin
from models import ReferenceContent, Page, SEOMetatag
#from django.db import models
#from vendor.ck.fields import CKEditor

import settings
import os

class SEOAdmin(admin.ModelAdmin):
    list_display = ('display_type', 'meta_title', 'meta_description', 'meta_keywords')

class ReferenceContentAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ('title', 'reference', 'display')
    list_filter = ('display',)

    class Media:
        js = (
            '/static/js/mootools.js',
            '/static/js/fckeditor/fckeditor.js',
            '/static/js/fckeditor.js',
        )

class PageAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'display')
    list_filter = ('display',)

#    formfield_overrides = {
#        models.TextField: {'widget' : CKEditor},
#    }

    class Media:
        js = (
            '/static/js/mootools.js',
            '/static/js/ckeditor/ckeditor.js',
            '/static/js/ckeditor.js',
        )

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'display', 'display_type')
    list_filter = ('display_type','display',)

admin.site.register(ReferenceContent, ReferenceContentAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(SEOMetatag, SEOAdmin)
