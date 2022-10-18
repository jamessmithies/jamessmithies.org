# See https://django-antispam.readthedocs.io/en/latest/usage.html for django anti-spam

from django import forms
from antispam.honeypot.forms import HoneypotField


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    spam_honeypot_field = HoneypotField()  

    