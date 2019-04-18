from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        usuario = authenticate(request, username=usuario, password=clave)
        if usuario:
            login(request, usuario)
            return redirect('post')
        else:
            return render(request, 'usuarios/login.html', {'error' : 'Usuario y contraseña no validos'})
    return render(request, 'usuarios/login.html')
