from django.shortcuts import render,get_object_or_404
from .models import perrito,user
from .form import PerritoForm,UserForm
from django.core import serializers
from django.http import HttpResponse,HttpResponseRedirect
import json

# Create your views here.

def indexlogin(request):
    return render(request, 'login.html')
    
def administrador(request):
    return render(request, 'index.html')

def usuario(request):
    return render(request, 'indexuser.html') 

def perro_list(request):
    perritos = perrito.objects.all()
    return render(request, 'listar_perros.html',{'perritoo':perritos})
    
def perro_list_user(request):
    perritoss = perrito.objects.all()
    return render(request, 'ver_perros.html',{'perritover':perritoss})

def perro_detalle(request, pk):
    perross = get_object_or_404(perrito, pk=pk)
    return render(request, 'detalle_perro.html', {'perros':perross})

def perro_eliminar(request, pk):
    perrito.objects.filter(pk=pk).delete()
    perros = perrito.objects.all()
    return render(request, 'index.html',{'perros':perros})

def perro_editar(request, pk):
    perro = get_object_or_404(perrito, pk=pk)
    if request.method == 'POST':
        form = PerritoForm(request.POST, instance=perro)
        if form.is_valid():
            perro = form.save(commit=False)
            perro.save()
            return HttpResponseRedirect('/perro/listar')
    else:
        form=PerritoForm(instance=perro)
        return render(request, 'editar_perro.html',{'form':form})


def perroo_nuevo(request):
    if request.method == 'POST':
        form = PerritoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/perro/listar')
    else:
        form = PerritoForm()
    return render(request, 'editar_perro.html',{'form': form})

def perroo_nuevo_user(request):
    if request.method == 'POST':
        form = PerritoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/perro/ver')
    else:
        form = PerritoForm()
    return render(request, 'editar_perro.html',{'form': form})

def user_nuevo(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/administrador')
    else:
        form = UserForm()
    return render(request, 'registerr_user.html',{'form': form})
