from django.shortcuts import render, redirect
from .models import Toner, Reservation

def aboutus(request):
    return render(request,'aboutus.html')

def home(request):
    Toners = Toner.objects.all
    if request.method == "GET":
        type = request.GET.get("recherche")
        if type is not None:
            Toners = Toner.objects.filter(type__icontains=type)

    return render(request,'acceuil.html',context={"Toners" : Toners})

def reservebus(request,pk ):
    toner = Toner.objects.get(id=pk)
    user = request.user
    if request.method == "POST":
        Reservation.objects.create(user=user, toner=toner)
        return redirect('remerciment')
    return render(request,'reservebus.html',{'toner':toner})

def remerciment(request):
    return render(request,'remerciment.html')
