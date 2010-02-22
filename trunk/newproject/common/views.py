
from django.shortcuts import render_to_response
from django.template import RequestContext

#from django.http import HttpResponseRedirect, HttpResponse
#from django.views.generic.simple import direct_to_template
#from django.core.urlresolvers import reverse

from forms import ContactForm
from emails import WebContactEmail, SendEmailError

from models import Page, ReferenceContent

#from django.core import serializers

import os
import settings

try:
    from settings_local import GOOGLE_MAPS_API_KEY, GOOGLE_API_STATUS, FLICKR_API_KEY, FLICKR_USER_ID
except ImportError:
    from settings import GOOGLE_MAPS_API_KEY, GOOGLE_API_STATUS, FLICKR_API_KEY, FLICKR_USER_ID

#----------------------------------
# VIEW METHODS
#----------------------------------

#
# URL: /
#
def home(request, reference="", template="home.html"): 
    context = {}

    context['view_title'] = 'home'

    try:
        context["referencecontent"] = ReferenceContent.objects.get(reference="home")
    except:
        print "No home reference content in the database."

     	return render_to_response(template, context, context_instance=RequestContext(request))

#----------------------------------]



#
# URL: /gallery/
#
def gallery(request, template="gallery.html"):
    context={}

    context['view_title'] = 'gallery'

    try:
        import flickrapi
        flickr = flickrapi.FlickrAPI(FLICKR_API_KEY)

        elems = flickr.photos_search(user_id=FLICKR_USER_ID, per_page='20')

        images = []
        for e in elems[0]:
            images.append(get_pic_url(
                size="thumb",
                farm=e.get("farm"),
                server=e.get("server"),
                id=e.get("id"),
                secret=e.get("secret")
            ))
        context["images"] = images
    except:
        print "Flickr Has Failed to Load."
    try:
        context["referencecontent"] = ReferenceContent.objects.get(reference="gallery")
    except:
        print "No gallery reference content in the database."

    return render_to_response(template, context, context_instance=RequestContext(request))

# FLICKR FUNCTION
# -----------------------------------

# Get URL to flickr image
# small_square=75x75
# thumb=100 on longest side
# small=240 on longest side
# medium=500 on longest side
# large=1024 on longest side
# original=duh
def get_pic_url(size, farm, server, id, secret):
    size_char='s'  # default to small_square

    if size == 'small_square':
        size_char='_s'
    elif size == 'thumb':
        size_char='_t'
    elif size == 'small':
        size_char='_m'
    elif size == 'medium':
        size_char=''
    elif size == 'large':
        size_char='_b'
    elif size == 'original':
        size_char='_o'

    return "http://farm%s.static.flickr.com/%s/%s_%s%s.jpg" % (farm, server, id, secret, size_char)

#----------------------------------]



#
# URL: /*slug*/
#
def page(request, slug="", template="flatpage.html"): 
    context = {}

    context['view_title'] = slug

    try:
        page = Page.objects.get(slug=slug)

        #setting the page's unique seo keywords
        if not page.meta_keywords == '':
            context['SEO_TITLE'] = page.meta_title
        if not page.meta_keywords == '':
            context['SEO_KEYWORDS'] = page.meta_keywords
        if not page.meta_description == '':
            context['SEO_DESCRIPTION'] = page.meta_description

        context['page'] = page
    except:
        print "There is no page with this slug in the database."

    return render_to_response(template, context, context_instance=RequestContext(request))
#----------------------------------]


#
# URL: /contact-us/
#
def contact(request, url_slug="", template="contact.html"): 
    context = {}

    context['view_title'] = 'contact'

    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST)
        if form.is_valid(): # All validation rules pass
            context['success'] = True
            try:
                WebContactEmail(
                    fullname = form.cleaned_data['fullname'],
                    email = form.cleaned_data['email'],
                    contact_number = form.cleaned_data['contact_number'],
                    comment = form.cleaned_data['comment']
                ).send()
            except SendEmailError, e:
                dict['success'] = False
    else:
        form = ContactForm()
    context['form'] = form

    try:
        context["referencecontent"] = ReferenceContent.objects.get(reference="contact")
    except:
        print "No contact reference content in the database."

    try:
        p = SEOMetatags.objects.get(display_type__exact="contact")
        dict['SEO_TITLE'] = p.meta_title
        dict['SEO_KEYWORDS'] = p.meta_keywords
        dict['SEO_DESCRIPTION'] = p.meta_description
    except:
        print "No contact seo metatags in the database."

    return render_to_response(template, context, context_instance=RequestContext(request))

#----------------------------------]
