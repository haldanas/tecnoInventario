#django
from django.contrib.auth.mixins import LoginRequiredMixin   
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from django.urls import reverse_lazy
#from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
#modelos
from django.contrib.auth.models import User


class HomeView(View):
    def get(self, request):        
        return render(request,'auth/user_home.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        #return render(request,'auth/user_home.html')
        return redirect('usuarios:login')

#class LoginView(View):
def loginView(request):
    if not request.user.is_anonymous:
        return redirect('usuarios:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        print("post")
        if user:
            if user.is_active:
                login(request, user)
                return redirect('usuarios:home')
            else:
                return render(request, 'auth/login.html',{'error':'Contraseña o clave no coinciden'})
        else:
            #return HttpResponseRedirect(settings.LOGIN_URL)
            return redirect('usuarios:home')
    return render(request, 'auth/login.html')

class PerfilList(ListView):
    model = User

class PerfilDetail(DetailView):
    model = User

class PerfilCreation(CreateView):
    model = User
    success_url = reverse_lazy('usuarios:list')
    fields = ['username','first_name','last_name', 'password', 'email']

class PerfilUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('usuarios:list')
    fields = ['username','first_name','last_name', 'password', 'email']


class PerfilDelete(DeleteView):
    model = User
    success_url = reverse_lazy('usuarios:list')