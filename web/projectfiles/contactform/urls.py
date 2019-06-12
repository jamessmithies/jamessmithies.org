from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

from . import views

app_name = "contactform"

urlpatterns = [
    url(r'^form/$', views.emailView, name='contact'),
    url(r'^success/$', views.successView, name='success'),

]

