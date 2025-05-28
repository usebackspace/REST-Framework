from django.urls import path
from . import views

urlpatterns = [
    path('avengers/',views.avenger),
    path('avengers/<int:pk>/',views.avenger_update),
    
]
