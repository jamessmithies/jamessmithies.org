from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import models
from . import views

urlpatterns = [
    url(r'^$', views.homepageView, name='home'),
    url(r'^tags/(?P<slug>[-\w]+)/$', views.virtualmachines_taglistView.as_view(), name="virtualmachines_tag_list"),
    url(r'^tags/$', views.virtualmachines_tagsView, name="tags"),
    url(r'^types/(?P<slug>[-\w]+)/$', views.virtualmachines_typelistView.as_view(), name="virtualmachines_type_list"),
    url(r'^types/$', views.virtualmachines_typesView, name="types"),
    url(r'^help/(?P<slug>.+)/$', views.HelpView, name='help'),
    url(r'^(?P<slug>.+)/$', views.SpecificationView, name='specification'), 
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)