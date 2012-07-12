from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from mysite.tabcollection.models import Song, Artist
from forms import SongForm

def index(request):
    return render_to_response('tabcollection/index.html', context_instance=RequestContext(request))

def latest(request):
    latest_song_list = Song.objects.all().order_by('title')[:5]
    return render_to_response('tabcollection/latest.html', {'latest_song_list':latest_song_list},
                              context_instance=RequestContext(request))

def song_detail(request, song_id):
    s = get_object_or_404(Song, pk=song_id)
    return render_to_response('tabcollection/song_detail.html', {'song':s},
                              context_instance=RequestContext(request))

def artist_detail(request, artist_id):
	a = get_object_or_404(Artist, pk=artist_id)
	songs = a.song_set.all()
	return render_to_response('tabcollection/artist_detail.html', {'artist':a, 'songs':songs},
								context_instance=RequestContext(request))

def search(request):
	if 'search_criteria' in request.GET and request.GET['search_criteria']:
		search_criteria = request.GET['search_criteria']
		message = 'You searched for %r' % search_criteria
		songResults = Song.objects.filter(title__icontains=search_criteria)
		artistResults = Artist.objects.filter(name__icontains=search_criteria)
		return render_to_response('tabcollection/search_results.html', {'songs':songResults, 
			'artists':artistResults, 'search_criteria':search_criteria }, 
			context_instance=RequestContext(request))
	else:
		message = 'You submitted an empty form'
		return HttpResponse(message)

def new_artist_form(req):
	return render_to_response('tabcollection/new_artist.html', {}, 
								context_instance=RequestContext(req))

def new_artist_submit(req):
	if 'artistName' in req.POST and req.POST['artistName']:
		name_param = req.POST['artistName']
		a = Artist(name=name_param)
		a.save()
		return index(req)
	else:
		message = 'You submitted an empty form'
		return HttpResponse(message)

def new_song_form(req):
	form = SongForm()
	return render_to_response('tabcollection/new_song.html', { 'form': form }, 
								context_instance=RequestContext(req))
    
def new_song_submit(req):
	if req.method == 'POST':
		form = SongForm(req.POST, req.FILES)
        print req
        if form.is_valid():
            handle_uploaded_mp3(req.FILES['mp3_file'])
            form.save()
            return index(req)
        else:
            print 'form is not valid'
            return render_to_response('tabcollection/new_song.html', { 'form': form }, 
								context_instance=RequestContext(req))

def handle_uploaded_mp3(f):
    with open(f.name, 'w') as destination:
        for chunk in f.chunks():
            destination.write(chunk)