# See https://django-antispam.readthedocs.io/en/latest/usage.html for django anti-spam
# See https://github.com/praekelt/django-recaptcha for django-recaptcha

from django import forms
from antispam.honeypot.forms import HoneypotField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible



class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    spam_honeypot_field = HoneypotField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)



    

    