from django.shortcuts import render
from .models import ChatRoom,ChatMessage
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def index(request):
    chatrooms = ChatRoom.objects.all()

    return render(request,'chatapp/index.html', {
        'chatrooms':chatrooms
    })

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,username = data['username'],
                password=data['password']
                )
            if user is not None:
                login(request, user)
                chatrooms = ChatRoom.objects.all()
                return render(request,'chatapp/index.html', {
                    'chatrooms':chatrooms
                })
            else:
                return HttpResponse("Invalid Credentials")
    else:
        form = LoginForm()
    return render(request,'chatapp/login.html', {
        'form':form
    })

def chatroom(request,slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    return render(request,'chatapp/room.html', {
        'chatroom':chatroom,
        'messages':messages,
    })

