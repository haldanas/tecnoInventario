#django
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
#from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
#modelos
from referencias.models import Referencia

class RefList(ListView):
    model = Referencia

class RefDetail(DetailView):
    model = Referencia

class RefCreation(CreateView):
    model = Referencia
    success_url = reverse_lazy('referencias:list')
    fields = ['nombre','marca','observacion']

class RefUpdate(UpdateView):
    model = Referencia
    success_url = reverse_lazy('referencias:list')
    fields = ['nombre','marca','observacion']


class RefDelete(DeleteView):
    model = Referencia
    success_url = reverse_lazy('referencias:list')