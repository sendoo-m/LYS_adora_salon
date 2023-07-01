from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
   

    class Meta:
        model = Booking
        exclude = ['is_approved']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        
        # Check if the chosen date and time combination is already booked
        if Booking.objects.filter(start_time=start_time).exists():
            self.add_error('start_time', 'This time slot is already booked.')

        return cleaned_data