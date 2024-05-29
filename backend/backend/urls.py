from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('stock', include('base.urls')),
    path('admin/', admin.site.urls),
    path('',include('accounts.urls'))
]
