#django
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
#from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
#modelos
from almacenes.models import Almacen
from almacenes.models import Inventario
import pandas as pd
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
    
class InvUpdate(UpdateView):
    model = Inventario
    success_url = reverse_lazy('inventarios:list')
    fields = ['almacen','referencia','cantidad']

class InvDelete(DeleteView):
    model = Inventario
    success_url = reverse_lazy('inventarios:list')

class InvCreation(CreateView):
    model = Inventario
    success_url = reverse_lazy('inventarios:list')
    fields = ['almacen','referencia','cantidad']
    
def entrada(request):
    if request.method == 'POST':
        filep = request.FILES['uploadedFile']
        xls = pd.ExcelFile(filep)
        df=xls.parse(xls.sheet_names[0])
        #print (df.head(8))
        print (df.columns.values)#3
        print (df.columns.values[1])#referencia
        print(df.index.values)
        print(df.index.values[3])
        return redirect('inventarios:list')
    