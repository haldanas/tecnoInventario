from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# django >> url http reques, settings urlconf >> url patherns busca el patch que marque >>  manda el (httpreq,) .


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
            return render(request, 'usuarios/login.html',{'error':'invalido'})
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