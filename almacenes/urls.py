from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import (
    AlmList,
    AlmDetail,
    AlmCreation,
    AlmUpdate,
    AlmDelete,
)

urlpatterns = [
    # Managment
    url(r'^almacenes/$', login_required(AlmList.as_view()), name='list'),
    url(r'^almacenes/(?P<pk>\d+)$', login_required(AlmDetail.as_view()), name='detail'),
    url(r'^almacenes/nuevo$', login_required(AlmCreation.as_view()), name='new'),
    url(r'^almacenes/editar/(?P<pk>\d+)$', login_required(AlmUpdate.as_view()), name='edit'),
    #url(r'^almacenes/borrar/(?P<pk>\d+)$', login_required(AlmDelete.as_view()), name='delete'),
]