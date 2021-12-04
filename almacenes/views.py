#django
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
#from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
#modelos
from almacenes.models import Almacen
from almacenes.models import Inventario

#Almacenes
class AlmList(ListView):
    model = Almacen

class AlmDetail(DetailView):
    model = Almacen

class AlmCreation(CreateView):
    model = Almacen
    success_url = reverse_lazy('almacenes:list')
    fields = ['nombre','direccion']

class AlmUpdate(UpdateView):
    model = Almacen
    success_url = reverse_lazy('almacenes:list')
    fields = ['nombre','direccion']

class AlmDelete(DeleteView):
    model = Almacen
    success_url = reverse_lazy('almacenes:list')

#Inventarios
class InvList(ListView):
    model = Inventario

class InvDetail(DetailView):
    model = Inventario
    
class InvCreation(CreateView):
    model = Inventario
    success_url = reverse_lazy('inventarios:list')
    fields = ['almacen','referencia','cantidad']

class InvUpdate(UpdateView):
    model = Inventario
    success_url = reverse_lazy('inventarios:list')
    fields = ['almacen','referencia','cantidad']

class InvDelete(DeleteView):
    model = Inventario
    success_url = reverse_lazy('inventarios:list')