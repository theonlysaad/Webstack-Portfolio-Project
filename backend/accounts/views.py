from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect


User = get_user_model()
def logout_user(request):
    logout(request)
    return redirect('login')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
    return render(request,'connexion.html')


def signup (request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        login(request,user)
        return redirect('home')

    return render(request,'inscription.html')
