from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('slider/', views.slider_view, name='slider'),
    path('services/', views.services, name='services'),
    path('booking_create/', views.booking_create, name='booking_create'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('is_approved/<int:booking_id>/', views.is_approved, name='is_approved'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)