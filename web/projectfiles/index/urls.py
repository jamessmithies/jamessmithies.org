from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

app_name = "index"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mastodonsidebar/$', views.mastodonsidebarView, name='mastodonsidebar'),
    url(r'^update-zotero/$', views.updatezoteroView, name='update_zotero'),
    url(r'^update-mastodon/$', views.updatemastodonView, name='update_mastodon'),
    url(r'^projects/$', views.projectsView, name='projects'),
    url(r'^bio/$', views.bioView, name='bio'),
    url(r'^research/$', views.researchView, name='research'),
    url(r'^design/$', views.designView, name='design'),
    url(r'^credits/$', views.creditsView, name='credits'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)