from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,get_object_or_404
from songs.models import Song


def index(request):
    latest_song_list = Song.objects.all().order_by('title')[:5]
    return render_to_response('songs/index.html',{'latest_song_list':latest_song_list})

def detail(request,song_id):
    s = get_object_or_404(Song,pk=song_id)
    return render_to_response('songs/detail.html',{'song':s},
                              context_instance=RequestContext(request))