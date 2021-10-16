from django.shortcuts import render

from .models import Destination
# Create your views here.

# def index(request):
#   return render(request,'index.html',{'price': 700})

# def index(request):

#   dest1 =  Destination()
#   dest1.name = 'Mumbai'
#   dest1.desc = "testing"
#   dest1.price = 700
#   dest1.img = 'img-04.jpg'
#   dest1.offer = False

#   dest2 = Destination()
#   dest2.name = 'Nashik'
#   dest2.desc = "Example"
#   dest2.price = 800
#   dest2.img = 'img-02.jpg'
#   dest2.offer = True

#   dest3 = Destination()
#   dest3.name = 'Chennai'
#   dest3.desc = "CSK"
#   dest3.price = 900
#   dest3.img = 'img-03.jpg'
#   dest3.offer = True
  
#   # print(dest1)
#   # return render(request, 'index.html', {'dest1': dest1, 'dest2': dest2, 'dest3': dest3})
  
#   dests = [dest1, dest2, dest3]
#   return render(request, 'index.html', {'dests': dests})


def index(request):

  dests = Destination.objects.all()

  return render(request, 'index.html', {'dests': dests})
