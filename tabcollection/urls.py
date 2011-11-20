from django.conf.urls.defaults import patterns, include, url
from django.views.static import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tabcollection.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'index'),
    (r'^song/(?P<song_id>\d+)/$', 'song_detail'),
    (r'^artist/(?P<artist_id>\d+)/$', 'artist_detail'),
    (r'^new-artist-form/$', 'new_artist_form'),
    (r'^new-artist-submit/$', 'new_artist_submit'),
    (r'^new-song-form/$', 'new_song_form'),
    (r'^new-song-submit/$', 'new_song_submit'),
    (r'^search/$', 'search'),
)
