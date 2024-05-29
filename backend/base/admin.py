from django.contrib import admin

# Register your models here.
from .models import Toner,Reservation

admin.site.register(Toner)
admin.site.register(Reservation)