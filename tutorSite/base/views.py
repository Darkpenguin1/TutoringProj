from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': "Lets learn Python"},
    {'id': 2, 'name': "Lets learn Design"},
    {'id': 3, 'name': "Lets learn Web Development"},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, "base/home.html", context)   # Specify the app and its templates folder basically blueprints in flask

def room(request, pk):
    room = None

    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    
    return render(request, "base/room.html", context)
