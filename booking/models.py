from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)
    start_time = models.TimeField()
    hair_care = models.BooleanField(default=False)
    face_care = models.BooleanField(default=False)
    body_care = models.BooleanField(default=False)
    all_services = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption