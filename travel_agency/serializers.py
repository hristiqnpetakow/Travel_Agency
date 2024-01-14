from rest_framework import serializers

from travel_agency.models import Locations, Holidays, Reservations


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ["street", "number", "city", "country"]


class HolidaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holidays
        fields = ["location", "title", "start_date", "duration", "price", "free_slots"]


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ["searchBy", "start_date", "duration"]