# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
import datetime
 
from models import Event
 
def events_index(request):
    '''a basic events listing view'''
    events = Event.objects.filter().order_by('-date')
    now = datetime.datetime.now()
 
    #create a dict with the years and months:events 
    event_dict = {}
    for i in range(events[0].date.year, events[len(events)-1].date.year-1, -1):
        event_dict[i] = {}
        for month in range(1,13):
            event_dict[i][month] = []
    for event in events:
        event_dict[event.date.year][event.date.month].append(event)
 
    #this is necessary for the years to be sorted
    event_sorted_keys = list(reversed(sorted(event_dict.keys())))
    list_events = []
    for key in event_sorted_keys:
        adict = {key:event_dict[key]}
        list_events.append(adict)
 
    t = loader.get_template('templates/event_index.html')
    c = Context({
       'now': now,'list_events':list_events,
    })
    return HttpResponse(t.render(c))
