from django.shortcuts import render

# Create your views here.
# django >> url http reques, settings urlconf >> url patherns busca el patch que marque >>  manda el (httpreq,) .
def lista_usuarios(request):
    return render(request, 'usuarios/usuarios.html')

def login_view(request):
    """Login view"""
    return render(request, 'usuarios/login.html')