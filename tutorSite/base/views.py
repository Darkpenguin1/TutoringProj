from django.shortcuts import render

# Create your views here.
from .models import Room


# how to query db
# queryset = modelname.objects.all()
# Var that stores the query
# modelname
# model objects attribute
# method, ex: get(), filter(), exclude()

# rooms = [
#     {'id': 1, 'name': "Lets learn Python"},
#     {'id': 2, 'name': "Lets learn Design"},
#     {'id': 3, 'name': "Lets learn Web Development"},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, "base/home.html", context)   # Specify the app and its templates folder basically blueprints in flask

def room(request, pk):  # primary key 
    room = Room.objects.get(id=pk)
    context = {"room": room}
    
    return render(request, "base/room.html", context)
