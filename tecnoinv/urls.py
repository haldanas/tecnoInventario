
from django.urls import path, include
from django.conf import settings
#  from django.http import HttpRequest
#hak para el desarollo de multimedia
from django.conf.urls.static import static

urlpatterns = [
    
    path('', include(('usuarios.urls', 'usuarios'), namespace='home')),
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# XXXX -->Esta linea es agregada como parte del hak de pruebas 
# para media se debio crear :
# MEDIA_URL = url despeus del host donde esta la media,b
# usqueda en nuestra midea (no url)
# MEDIA_ROOT = path absoluto de la media
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)