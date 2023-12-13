from django.urls import path
from . import views

urlpatterns = [
    path('courts/', views.courts, name='courts'),
    path('courts/details/<int:id>', views.court_details, name='court_details'),
]