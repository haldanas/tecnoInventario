from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from .views import (
    RefList,
    RefDetail,
    RefCreation,
    RefUpdate,
    RefDelete,
)

urlpatterns = [
    # Managment
    url(r'^referencias/$', login_required(RefList.as_view()), name='list'),
    url(r'^referencias/(?P<pk>\d+)$', login_required(RefDetail.as_view()), name='detail'),
    url(r'^referencias/nuevo$', login_required(RefCreation.as_view()), name='new'),
    url(r'^referencias/editar/(?P<pk>\d+)$', login_required(RefUpdate.as_view()), name='edit'),
    #url(r'^referencias/borrar/(?P<pk>\d+)$', login_required(RefDelete.as_view()), name='delete'),
]