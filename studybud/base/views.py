from django.shortcuts import render


rooms=[
    {'id':1, 'name':'learn python'},
    {'id':2, 'name':'learn django'},
    {'id':3, 'name':'learn react'},
    
]

def home(request):
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room=None
    for r in rooms:
        if r['id']==int(pk):
            room=r
    context={'room':room}
    return render(request, 'base/room.html',context)