from django.db import models


# Create your models here.
class Locations(models.Model):
    street = models.CharField(max_length=77)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=77)
    country = models.CharField(max_length=77)

    class Meta:
        db_table = "locations"


class Holidays(models.Model):
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    title = models.CharField(max_length=77)
    start_date = models.DateField()
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    free_slots = models.PositiveIntegerField()

    class Meta:
        db_table = "holidays"


class Reservations(models.Model):
    searchBy = models.ForeignKey(Holidays, on_delete=models.CASCADE)
    start_date = models.DateField()
    duration = models.PositiveIntegerField()

    class Meta:
        db_table = "reservations"

