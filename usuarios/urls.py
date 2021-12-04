from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from .views import (
    HomeView,
    LogoutView,
    PerfilList,
    PerfilDetail,
    PerfilCreation,
    PerfilUpdate,
    PerfilDelete,
)

urlpatterns = [
    # Managment
    path(route= '',view = views.loginView, name='login'),
    # path(route='actualizar_perfil/', view=views.actualizarPerfil, name='actualizar_perfil'),
    url(r'^logout$', login_required(LogoutView.as_view()), name='logout'),
    url(r'^home$', login_required(HomeView.as_view()), name='home'),
    url(r'^usuarios/$', login_required(PerfilList.as_view()), name='list'),
    url(r'^usuarios/(?P<pk>\d+)$', login_required(PerfilDetail.as_view()), name='detail'),
    url(r'^usuarios/nuevo$', login_required(PerfilCreation.as_view()), name='new'),
    url(r'^usuarios/editar/(?P<pk>\d+)$', login_required(PerfilUpdate.as_view()), name='edit'),
    url(r'^usuarios/borrar/(?P<pk>\d+)$', login_required(PerfilDelete.as_view()), name='delete'),
]