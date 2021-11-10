"""tecnoinv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tecnoinv import settings, veiws as localviwes
from usuarios import views as usuarios_views
from django.conf import settings
#  from django.http import HttpRequest
#hak para el desarollo de multimedia
from django.conf.urls.static import static

urlpatterns = [
    #path('hello/', localviwes.hello, name='hello_world'),
    path('usuarios/login/', usuarios_views.login_view, name='login'),
    #path('admin/', admin.site.urls),
    
    
    #path('', include(('posts.urls', 'posts'), namespace='posts')),
    
    #path('admin/', admin.site.urls, name='admin'),
    #path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# XXXX -->Esta linea es agregada como parte del hak de pruebas 
# para media se debio crear :
# MEDIA_URL = url despeus del host donde esta la media,b
# usqueda en nuestra midea (no url)
# MEDIA_ROOT = path absoluto de la media
#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)