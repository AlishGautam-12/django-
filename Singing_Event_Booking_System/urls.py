from django.contrib import admin
from django.urls import path
from Singing_Event_Booking_System import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('Home/', views.Home, name='Home'),  
    path('Product/', views.Product, name='Product'),
    path('add_event/', views.add_event, name='add_event'),
    path('event_list/', views.event_list, name='Event_list'),
    path('event/<int:pk>/update/', views.event_update, name='update_event'),
    path('event/<int:pk>/delete/', views.event_delete, name='delete_event'),
    path('book_now/', views.book_now_submit, name='book_now_submit'),
    path('My_Booking/', views.My_Booking, name='My_Booking'),
    path('update_booking/<int:pk>/', views.update_booking, name='update_booking'),
    path('delete_booking/<int:pk>/', views.delete_booking, name='delete_booking'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)