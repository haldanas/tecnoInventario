from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
#  from django.http import HttpRequest
#hak para el desarollo de multimedia
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #path('', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    url(r'^', include(('usuarios.urls','usuarios'), namespace='usuarios')),
    #path('', include(('referencias.urls', 'referencias'), namespace='referencias')),
    url(r'^', include(('referencias.urls','referencias'), namespace='referencias')),
    #path('', include(('almacenes.urls', 'almacenes'), namespace='almacenes')),
    url(r'^', include(('almacenes.urls','almacenes'), namespace='almacenes')),
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# XX -->Esta linea es agregada como parte del hak de pruebas 
# para media se debio crear :
# MEDIA_URL = url despeus del host donde esta la media,b
# usqueda en nuestra midea (no url)
# MEDIA_ROOT = path absoluto de la media
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)