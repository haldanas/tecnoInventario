from django.urls import path
from . import views

urlpatterns = [
    # Managment
    path(route= '',view = views.login_view , name='login'),
    path(route= 'home/',view = views.home_view , name='home'),
    #path('singup/', views.SignupView.as_view(), name='singup'),
    path(route='logout/', view=views.logout_view, name='logout'),
    path(route='registro/', view=views.registro_view, name='registro'),
    path(route='actualizar_perfil/', view=views.actualizarPerfil, name='actualizar_perfil'),
]