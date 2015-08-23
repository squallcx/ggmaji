from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, hotel

def detail(request, hotel_id):
    try:
        hotel = hotel.objects.get(pk=hotel_id)
    except hotel.DoesNotExist:
        raise Http404("hotel does not exist")
    return render(request, 'myshop/detail.html', {'hotel': hotel})

class IndexView(generic.ListView):
    template_name = 'myshop/index.html'
    context_object_name = 'latest_hotel_list'

    def get_queryset(self):
        """Return the last five published hotels."""
        return hotel.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = hotel
    template_name = 'myshop/detail.html'


class ResultsView(generic.DetailView):
    model = hotel
    template_name = 'myshop/results.html'

def results(request, hotel_id):
    hotel = get_object_or_404(hotel, pk=hotel_id)
    return render(request, 'myshop/results.html', {'hotel': hotel})

def vote(request, hotel_id):
    p = get_object_or_404(hotel, pk=hotel_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'myshop/detail.html', {
            'hotel': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('myshop:results', args=(p.id,)))
"""
def index(request):
    return HttpResponse("Hello, world. You're at the myshop index.")

def detail(request, hotel_id):
    return HttpResponse("You're looking at hotel %s." % hotel_id)

def results(request, hotel_id):
    response = "You're looking at the results of hotel %s."
    return HttpResponse(response % hotel_id)

def vote(request, hotel_id):
    return HttpResponse("You're voting on hotel %s." % hotel_id)
"""
