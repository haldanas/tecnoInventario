from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def almacenes_view(request):
    return render(request, 'almacenes/almacen.html')
