from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.dates import ArchiveIndexView, DateDetailView

from . import views
from . import models
from . import feeds

app_name = "blog"

urlpatterns = [
    url(r'^$', views.blogindexView, name='home_list'), 
    url(r'^(?P<selected_page>\d+)/?$', views.blogindexView, name='home_list'), 
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.entryView, name='entry'),  
    url(r'^categories/(?P<slug>[-\w]+)/$', views.categorylistView, name="category_list"),
    url(r'^categories/(?P<slug>[-\w]+)/(?P<selected_page>\d+)/?$', views.categorylistView, name="category_list"),
    url(r'^categories/$', views.categoriesView, name="categories"),
    url(r'^tags/(?P<slug>[-\w]+)/$', views.taglistView.as_view(), name="tag_list"),
    url(r'^tags/$', views.tagsView, name="tags"),
    url(r'^archive/', ArchiveIndexView.as_view(model=models.Entry, date_field="pub_date"), name="entry_archive"),
    url(r'^feed/$', feeds.LatestEntriesFeed()),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)