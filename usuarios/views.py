from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

# Create your views here.
# django >> url http reques, settings urlconf >> url patherns busca el patch que marque >>  manda el (httpreq,) .
def lista_usuarios(request):
    return render(request, 'usuarios/usuarios.html')

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        
        usuario = authenticate(request, username= usuario,
                               password=clave)
        if usuario:
            login(request, usuario )
            return redirect('usuarios:detail')
        else:
            return render(request, 'usuarios/login.html',{'error':'invalido'})
    return render(request, 'home.html')