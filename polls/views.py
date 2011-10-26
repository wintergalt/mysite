# Create your views here.

from django.http import HttpResponse
#from django.template import Context,loader
from polls.models import Poll
from django.shortcuts import render_to_response,get_object_or_404

#def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    t = loader.get_template('polls/index.html')
#    c = Context({
#                 'latest_poll_list': latest_poll_list, 
#    })
#    return HttpResponse(t.render(c))
'''
It's a very common idiom to load a template, fill a context and return
 an HttpResponse object with the result of the rendered template. Django 
 provides a shortcut. Here's the full index() view, rewritten:
'''
def index(request):
    latest_poll_list = Poll.object.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html',{'latest_poll_list':latest_poll_list})
    
def detail(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    return render_to_response('polls/detail.html',{'poll':p})

def results(request,poll_id):
    return HttpResponse('You are looking at the results of poll %s.' % poll_id)

def vote(request,poll_id):
    return HttpResponse('You are voting on poll %s.' % poll_id)