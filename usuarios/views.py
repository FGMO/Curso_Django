from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from usuarios.models import Perfil

from django.db.utils import IntegrityError

# Create your views here.

def registro(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        clave = request.POST['clave']
        confirma_clave = request.POST['confirma_clave']
        if clave != confirma_clave:
            return render(request, 'usuarios/registro.html', {'error': 'Las contraseñas no coinciden.'})
        try:
            usuario = User.objects.create_user(username=usuario, password=clave)
        except IntegrityError:
            return render(request, 'usuarios/registro.html', {'error': 'El nombre de usuario ya esta en uso.'})            
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo
        usuario.save()

        perfil = Perfil(usuario=usuario)
        perfil.save()

        return redirect('login')

    return render(request, 'usuarios/registro.html')

def actualizar(request):
    return render(request, 'usuarios/actualizar.html')

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        usuario = authenticate(request, username=usuario, password=clave)
        if usuario:
            login(request, usuario)
            return redirect('post')
        else:
            return render(request, 'usuarios/login.html', {'error' : 'Usuario y contraseña no validos'})
    return render(request, 'usuarios/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')