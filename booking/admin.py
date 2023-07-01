from django.contrib import admin
from .models import SliderImage
from .models import Booking

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'is_approved', 'phone_number')
    list_filter = ('is_approved', )
    search_fields = ('name', 'phone_number')

admin.site.register(Booking, BookingAdmin)


admin.site.register(SliderImage)
