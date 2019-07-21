from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^djga/', include('google_analytics.urls')),

    url(r'^', include('index.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^virtualmachines/', include('virtualmachines.urls')),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    url(r'^contact/', include('contactform.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
 