from django.urls import path
from . import views

urlpatterns = [
    # Managment
    path(route= '',view = views.login_view , name='login'),
    path(route= 'usuarios/home/',view = views.home_view , name='home'),
    #path('singup/', views.SignupView.as_view(), name='singup'),
    path(route='logout/', view=views.logout_view, name='logout'),
]


