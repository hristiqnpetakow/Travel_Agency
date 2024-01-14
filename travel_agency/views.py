from rest_framework import generics
from .models import Locations, Holidays, Reservations
from .serializers import LocationsSerializer, HolidaysSerializer, ReservationsSerializer


class LocationsListView(generics.ListCreateAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer


class LocationsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer


class HolidaysListView(generics.ListCreateAPIView):
    queryset = Holidays.objects.all()
    serializer_class = HolidaysSerializer


class HolidaysDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holidays.objects.all()
    serializer_class = HolidaysSerializer


class HolidaysQueryView(generics.ListAPIView):
    serializer_class = HolidaysSerializer

    def get_queryset(self):
        queryset = Holidays.objects.all()

        location = self.request.query_params.get('location')
        if location:
            queryset = queryset.filter(location=location)

        start_date = self.request.query_params.get('startDate')
        if start_date:
            queryset = queryset.filter(start_date=start_date)

        duration = self.request.query_params.get('duration')
        if duration:
            queryset = queryset.filter(duration=duration)

        return queryset


class ReservationsListView(generics.ListCreateAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer


class ReservationsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservations.objects.all()
    serializer_class = ReservationsSerializer
