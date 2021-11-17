from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# django >> url http reques, settings urlconf >> url patherns busca el patch que marque >>  manda el (httpreq,)
# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from usuarios.models import Perfil

@login_required
def registro_view(request): 
    print(request)
    
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        passwd_confirmation = request.POST['password_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'usuarios/registro.html', {'error': 'Password confirmation does not match'})

        try:
            usuario_nuevo = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'usuarios/registro.html', {'error': 'Username is already in user'})

        # usuario.first_name = request.POST['first_name']
        # usuario.last_name = request.POST['last_name']
        usuario_nuevo.email = request.POST['email']
        usuario_nuevo.save()

        perfil = Perfil(usuario=usuario_nuevo)
        perfil = Perfil(cargo='nuevo')
        perfil.save()

        return redirect('usuarios:login')
    return render(request,'usuarios/registro.html')


def login_view(request):        
    """Login view"""
    if request.method == 'POST':
        
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        
        usuario = authenticate(request, username= usuario,
                               password=clave)
        if usuario:
            login(request, usuario )
            return redirect('usuarios:home')
        else:
            return render(request, 'usuarios/login.html',{'error':'Contraseña o clave no coinciden'})
    return render(request, 'usuarios/login.html')


@login_required
def home_view(request):
    return render(request, 'usuarios/home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

@login_required
def lista_usuarios(request):
    return render(request, 'usuarios/usuarios.html')