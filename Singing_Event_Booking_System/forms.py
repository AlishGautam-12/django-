from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'description', 'date', 'time', 'venue', 'price', 'image']

# forms.py



from .models import Booking


class BookingForm(forms.ModelForm):
    event_name = forms.CharField(max_length=255, required=True)  # Add event_name field

    class Meta:
        model = Booking
        fields = ['event_name', 'user_name', 'email', 'phone', 'description']