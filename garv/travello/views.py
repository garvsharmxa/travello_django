from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Jaipur'
    dest1.desc = 'The city of Jaipur, where every street has a story to tell.'
    dest1.price = 3299
    dest1.img = 'destination_7.jpg'

    dest2 = Destination()
    dest2.name = 'Mumbai'
    dest2.desc = 'Mumbai, where dreams come to life.'
    dest2.price = 3599
    dest2.img = 'destination_8.jpg'

    dest3 = Destination()
    dest3.name = 'Goa'
    dest3.desc = 'Goa - a land of sun, sand, and sea.'
    dest3.price = 3799
    dest3.img = 'destination_9.jpg'

    dests = [dest1,dest2,dest3]


    return render(request, 'index.html', {'dests' : dests})