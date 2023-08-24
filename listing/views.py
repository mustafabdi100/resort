from django.shortcuts import render,get_object_or_404, redirect
from .models import Room, Event, AboutUsContent

def home(request):
    about_content = AboutUsContent.objects.first()
    rooms = Room.objects.all()[:4]
    featured_events = Event.objects.all()[:2]
    return render(request, 'listing/home.html', {'about_content': about_content, 'rooms': rooms, 'featured_events': featured_events})


def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'listing/rooms.html',{'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    context = {
        'room': room,
    }
    return render(request, 'listing/room_detail.html', context)

def  events(request):
    events= Event.objects.all()
    return render(request, 'listing/events.html',{'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'listing/event_detail.html', {'event': event})


def about_us(request):
    about_content = AboutUsContent.objects.first()
    return render(request, 'listing/about-us.html', {'about_content': about_content})

def contact(request):
    if request.method == 'POST':
        # Process the form submission (you can add your logic here)
        
        # Redirect to the 'home' URL after form submission
        return redirect('home')

    return render(request, 'listing/contact.html')

