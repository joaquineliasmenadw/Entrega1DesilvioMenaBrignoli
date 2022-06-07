from django.shortcuts import render
from django.http import HttpResponse
from Hammer.models import Contacto,Empleado,Empleador,Servicio
from Hammer.forms import *

def hammer(request):
    empleados = Empleado.objects.all
    empleadores = Empleador.objects.all
    servicios = Servicio.objects.all
    context ={'empleados' : empleados, 'servicios' : servicios, 'empleadores' : empleadores}
    return render(request,'index.html',context)

def contacto(request):
    if request.method == 'GET':
        form = Contacto_form()
        context = {'form':form}
        return render(request, 'contacto.html', context=context)
    else:
        form = Contacto_form(request.POST)
        if form.is_valid():
            new_contacto = Contacto.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                telefono = form.cleaned_data['telefono'],
                email = form.cleaned_data['email'],
            )
            form2 = Contacto_form()
            context ={'new_contacto':new_contacto,'form2':form2}
        return render(request, 'contacto.html', context=context)

def create_empleado_view(request):
    if request.method == 'GET':
        form = Empleado_form()
        context = {'form':form}
        return render(request, 'create_empleado.html', context=context)
    else:
        form = Empleado_form(request.POST)
        if form.is_valid():
            new_empleado = Empleado.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],
                provincia = form.cleaned_data['provincia'],
                ciudad = form.cleaned_data['ciudad'],
                telefono = form.cleaned_data['telefono'],
                email = form.cleaned_data['email'],
                experiencia = form.cleaned_data['experiencia'],
            )
            form2 = Empleado_form()
            context ={'new_empleado':new_empleado,'form2':form2}
        return render(request, 'create_empleado.html', context=context)
    
def create_empleador_view(request):
    if request.method == 'GET':
        form = Empleador_form()
        context = {'form':form}
        return render(request, 'create_empleador.html', context=context)
    else:
        form = Empleador_form(request.POST)
        if form.is_valid():
            new_empleador = Empleador.objects.create(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],
                provincia = form.cleaned_data['provincia'],
                ciudad = form.cleaned_data['ciudad'],
                telefono = form.cleaned_data['telefono'],
                email = form.cleaned_data['email'],
            )
            form2 = Empleador_form()
            context ={'new_empleador':new_empleador,'form2':form2}
        return render(request, 'create_empleador.html', context=context)

def create_servicio_view(request):
    if request.method == 'GET':
        form = Servicio_form()
        context = {'form':form}
        return render(request, 'create_servicio.html', context=context)
    else:
        form = Servicio_form(request.POST)
        if form.is_valid():
            new_servicio = Servicio.objects.create(
                nombre = form.cleaned_data['nombre'],
                descripcion = form.cleaned_data['descripcion'],
                precio = form.cleaned_data['precio'],
                provincia = form.cleaned_data['provincia'],
                ciudad = form.cleaned_data['ciudad'],
                empleado = form.cleaned_data['empleado'],
                active = form.cleaned_data['active'],
            )
            form2 = Servicio_form()
            context ={'new_servicio':new_servicio,'form2':form2}
        return render(request, 'create_servicio.html', context=context)

def search_servicio_view(request):
    servicios = Servicio.objects.filter(nombre__contains = request.GET['search'])
    context = {'servicios':servicios}
    return render(request, 'search_servicio.html', context = context)
