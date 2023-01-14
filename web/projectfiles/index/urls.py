from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

app_name = "index"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/update-zotero-writing/$', views.updatezoterowritingView, name='update_zotero_writing'),
    url(r'^admin/update-zotero-talks/$', views.updatezoterotalksView, name='update_zotero_talks'),
    url(r'^projects/$', views.projectsView, name='projects'),
    url(r'^bio/$', views.bioView, name='bio'),
    url(r'^research/$', views.researchView, name='research'),
    url(r'^design/$', views.designView, name='design'),
    url(r'^credits/$', views.creditsView, name='credits'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)