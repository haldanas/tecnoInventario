from django.urls import path
from . import views

urlpatterns = [
    # Managment
    path(route= 'almacen/',view = views.almacenes_view , name='almacen'),
    #path('singup/', views.SignupView.as_view(), name='singup'),
]


