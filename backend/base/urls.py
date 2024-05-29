from django.urls import path
from .views import home, remerciment, reservebus, aboutus

urlpatterns=[
    path('stock', home, name='home'),
    path('remerciment/', remerciment, name="remerciment"),
    path('aboutus/', aboutus, name="aboutus"),
    path('reservebus/<int:pk>', reservebus, name="reservebus"),
]