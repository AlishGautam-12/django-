from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect ,get_object_or_404
from .forms import EventForm 
from .models import Event
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
# Create your views here.
@login_required(login_url='login')

def Home(request):
    return render(request, 'Home.html') 

def Product(request):
    events = Event.objects.all()  # Fetch all events from the database
    return render(request, 'product.html', {'events': events})
 
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Event added successfully:', form.cleaned_data)
            return redirect('Product')  
        else:
            # Print form errors for debugging
            print('Form errors:', form.errors)    
          
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'Event_list.html', {'events': events})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('Event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('Event_list')
    return render(request, 'delete_event.html', {'event': event})


def My_Booking(request):
    bookings = Booking.objects.all()  # Fetch all bookings from the database
    return render(request, 'My_Booking.html', {'bookings': bookings})


def book_now_submit(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking successful!')
            return redirect('My_Booking')
        else:
            messages.error(request,'')
    else:
        form = BookingForm()
    
    return render(request, 'book_now.html', {'form': form})

def book_now(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking successful!')
            return redirect('My_Booking') # Redirect to My_Booking page after successful booking
        else:
            messages.error(request, '')
    else:
        form = BookingForm()
    
    return render(request, 'book_now.html', {'form': form})



def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('My_Booking')  # Redirect to My_Booking page after update
        else:
            messages.error(request, '')
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'update_booking.html', {'form': form})

def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('My_Booking')  # Redirect to My_Booking page after deletion
    
    return render(request, 'delete_booking.html', {'booking': booking})