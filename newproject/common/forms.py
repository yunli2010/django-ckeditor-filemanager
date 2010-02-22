from django import forms

# Contact Us Form
class ContactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    contact_number = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea())
