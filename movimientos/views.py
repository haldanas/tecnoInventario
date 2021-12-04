#django
from django.urls import reverse_lazy
#from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
#modelos
from movimientos.models import Movimiento

class MovList(ListView):
    model = Movimiento

class MovDetail(DetailView):
    model = Movimiento

class MovCreation(CreateView):
    model = Movimiento
    success_url = reverse_lazy('movimientos:list')
    fields = ['nombre','operador','tipo']

class MovUpdate(UpdateView):
    model = Movimiento
    success_url = reverse_lazy('movimientos:list')
    fields = ['nombre','operador','tipo']


class MovDelete(DeleteView):
    model = Movimiento
    success_url = reverse_lazy('movimientos:list')