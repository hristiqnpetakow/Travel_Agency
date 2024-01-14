from django.urls import path
from .views import LocationsListView, LocationsDetailView, HolidaysListView, HolidaysDetailView, ReservationsListView, \
    ReservationsDetailView, HolidaysQueryView

urlpatterns = [
    path('locations/', LocationsListView.as_view(), name='locations-list'),
    path('locations/<int:pk>/', LocationsDetailView.as_view(), name='locations-detail'),

    path('holidays/', HolidaysListView.as_view(), name='holidays-list'),
    path('holidays/<int:pk>/', HolidaysDetailView.as_view(), name='holidays-detail'),
    path('holidays/query/', HolidaysQueryView.as_view(), name='holidays-query'),

    path('reservations/', ReservationsListView.as_view(), name='reservations-list'),
    path('reservations/<int:pk>/', ReservationsDetailView.as_view(), name='reservations-detail'),
]