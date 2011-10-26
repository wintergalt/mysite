# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from polls.models import Poll,Choice
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
    return render_to_response('polls/detail.html',{'poll':p},
                              context_instance=RequestContext(request))

def results(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    return render_to_response('polls/results.html', {'poll':p})
    return HttpResponse('You are looking at the results of poll %s.' % poll_id)

def vote(request,poll_id):
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form
        return render_to_response('polls/detail.html', {
            'poll':p,
            'error_message':'You did not select a choice',
            }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
    