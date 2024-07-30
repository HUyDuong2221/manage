from django.shortcuts import render
from .models import Room, Department
# Create your views here.

def list_room(request):
    list_room = Room.objects.all()
    dpm = Department.objects.all()
    print(list_room, dpm)
    return render(request, 'room/list_room.html', 
                  {"room" : list_room,
                  'dpm' : dpm})
