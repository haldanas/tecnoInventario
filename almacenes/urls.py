from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from .views import (
    AlmList,
    AlmDetail,
    AlmCreation,
    AlmUpdate,
    AlmDelete,
    InvCreation,
    InvList,
    InvDetail,
    InvUpdate,
    InvDelete,    
)

urlpatterns = [
    # Managment
    url(r'^almacenes/$', login_required(AlmList.as_view()), name='list'),
    url(r'^almacenes/(?P<pk>\d+)$', login_required(AlmDetail.as_view()), name='detail'),
    url(r'^almacenes/nuevo$', login_required(AlmCreation.as_view()), name='new'),
    url(r'^almacenes/editar/(?P<pk>\d+)$', login_required(AlmUpdate.as_view()), name='edit'),
    #url(r'^almacenes/borrar/(?P<pk>\d+)$', login_required(AlmDelete.as_view()), name='delete'),
    url(r'^inventarios/$', login_required(InvList.as_view()), name='list'),
    url(r'^inventarios/(?P<pk>\d+)$', login_required(InvDetail.as_view()), name='detail'),
    url(r'^inventarios/nuevo$', login_required(InvCreation.as_view()), name='new'),
    url(r'^inventarios/editar/(?P<pk>\d+)$', login_required(InvUpdate.as_view()), name='edit'),
    url(r'^inventarios/borrar/(?P<pk>\d+)$', login_required(InvDelete.as_view()), name='delete'),
    path(route= 'inventarios',view = views.entrada, name='entrada'),    
]