from django.core.mail import EmailMessage
from django.shortcuts import render_to_response
import settings
import time
import os

class SendEmailError(Exception):
    pass

class WebContactEmail(object):
    def __init__(self, **kwargs):
        try:
            self.fullname = kwargs['fullname']
        except:
            raise SendEmailError("Fullname required")

        try:
            self.email = kwargs['email']
        except:
            raise SendEmailError("email required")

        try:
            self.contact_number = kwargs['contact_number']
        except:
            raise SendEmailError("Contact number required")

        try:
            self.comment = kwargs['comment']
        except:
            raise SendEmailError("Comment required")

    def send(self):
        subject = ("Contact ~ %s") % settings.PROJECT_DOMAIN
        html_content = render_to_response('emails/web_contact.html', {
            'fullname': self.fullname,
            'email': self.email,
            'contact_number': self.contact_number,
            'comment': self.comment,
            'project': settings.PROJECT_DOMAIN
        }).content
        
        msg = EmailMessage(subject, html_content, settings.EMAIL_SYSTEM_SENDER, settings.WEBCONTACT_RECIPIENTS)
        msg.content_subtype = "html"
        
        try:
            if not settings.EMAIL_TEST_MODE: msg.send(fail_silently = False)
            
            else: # save the email to disk for manual inspection
                filename = os.path.join( settings.TEST_EMAIL_DIR, "%s_WebContactEmail.eml" % time.time().__int__().__str__() )
                if not os.path.isdir(settings.TEST_EMAIL_DIR): os.mkdir(settings.TEST_EMAIL_DIR)
                f = open(filename, 'w')
                f.write(msg.message().as_string())
                f.close()
                
        except Exception, e:
            print "Exception: %s" % e
            raise SendEmailError