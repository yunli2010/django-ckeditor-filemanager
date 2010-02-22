from datetime import datetime
from django.conf import settings
from django.core.cache import cache
from models import SEOMetatag

def commonModels(request):
    context={}
    try:
        p = SEOMetatag.objects.get(display_type__exact="global")
        context['SEO_TITLE'] = p.meta_title
        context['SEO_KEYWORDS'] = p.meta_keywords
        context['SEO_DESCRIPTION'] = p.meta_description
    except:
        pass
    return context