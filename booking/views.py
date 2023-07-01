from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import SliderImage
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    images = SliderImage.objects.all()
    context = {'images': images}
    return render(request, 'home.html', context)

def slider_view(request):
    images = SliderImage.objects.all()
    return render(request, 'slider.html', {'images': images})

def services(request):
    images = SliderImage.objects.all()
    context = {'images': images}
    
    return render(request, 'services.html', context)


def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
        images = SliderImage.objects.all()
    
    context = {
        'form': form,
        'images': images,
    
    }
    return render(request, 'booking_create.html', context)

def booking_success(request):
    return render(request, 'booking_success.html')


@login_required(login_url='login')
def dashboard(request):
    bookings = Booking.objects.all()
    paginator = Paginator(bookings, 10)  # Display 10 bookings per page
    images = SliderImage.objects.all()
    page_number = request.GET.get('page')
    bookings = paginator.get_page(page_number)

    context = {
        'bookings': bookings,
        'images': images,
    }
    return render(request, 'dashboard.html', context)



def is_approved(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        is_approved = request.POST.get('is_approved')
        if is_approved:
            booking.is_approved = True
        else:
            booking.is_approved = False
        booking.save()
    return redirect('dashboard')

def about(request):
    images = SliderImage.objects.all()
    context = {'images': images}
    return render(request, 'about.html', context)


def contact(request):
    images = SliderImage.objects.all()
    context = {'images': images}
    return render(request, 'contact.html', context)


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Replace with the actual template name for your login page


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
