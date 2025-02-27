from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing
def index(request):
    # return HttpResponse('<h1>Testing BTRE home page</h1>')
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3] # use - in front of list_date in order to get descending order
    context= {
        'listings':listings,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'state_choices':state_choices
    }
    return render(request, 'pages/index.html',context)
def about(request):
    return render(request, 'pages/about.html')