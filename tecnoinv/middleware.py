from django.shortcuts import redirect
from django.urls import reverse

import usuarios


class PerfilCompletoMiddleware:
    def __init__(self, get_response):
        
        self.get_response = get_response

    def __call__(self, request):
        
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                perfil = request.user.perfil
                if not perfil.cargo:
                    if request.path not in [reverse('usuarios:actualizar_perfil'), reverse('usuarios:logout')]:
                        return redirect('usuarios:actualizar_perfil')

        response = self.get_response(request)
        return response 