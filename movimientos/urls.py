from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from .views import (
    MovList,
    MovDetail,
    MovCreation,
    MovUpdate,
    MovDelete,
)

urlpatterns = [
    # Managment
    url(r'^movimientos/$', login_required(MovList.as_view()), name='list'),
    url(r'^movimientos/(?P<pk>\d+)$', login_required(MovDetail.as_view()), name='detail'),
    url(r'^movimientos/nuevo$', login_required(MovCreation.as_view()), name='new'),
    url(r'^movimientos/editar/(?P<pk>\d+)$', login_required(MovUpdate.as_view()), name='edit'),
    #url(r'^movimientos/borrar/(?P<pk>\d+)$', login_required(MovDelete.as_view()), name='delete'),
]