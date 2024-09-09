from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
from .models import Room, Topic
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

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')




    context = {}
    return render(request, 'base/login_register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        ) # while typing if the typed string atleast contains certain amount of letters for ex py

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms':rooms, 'topics':topics, 'room_count':room_count,}
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