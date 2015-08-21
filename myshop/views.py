from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from .models import hotel,choice


def index(request):
    latest_hotel_list = hotel.objects.order_by('-pub_date')[:5]
    context = {'latest_hotel_list': latest_hotel_list}
    return render(request, 'myshop/index.html', context)

def vote(request, hotel_id):
    p = get_object_or_404(hotel, pk=hotel_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the hotel voting form.
        return render(request, 'myshop/detail.html', {
            'hotel': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
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
