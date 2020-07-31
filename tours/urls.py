from django.urls import path
from .views import MainView, DepartureView, TourView

urlpatterns = [
    path('tours/<int:id>/', TourView.as_view()),
    path('departures/<str:departure>/', DepartureView.as_view()),
    path('', MainView.as_view()),
]
