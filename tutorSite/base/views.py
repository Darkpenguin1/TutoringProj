from django.shortcuts import render, redirect

# Create your views here.
from .models import Room
from .forms import RoomForm
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

def create_room(request):
    form = RoomForm()
    context = {'form':form}
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "base/room_form.html", context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, "base/room_form.html", context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, "base/delete.html", {'obj': room})