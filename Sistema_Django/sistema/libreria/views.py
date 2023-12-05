from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.contrib import messages
# Create your views here.

def inicio(request):
    return render(request, 'index.html')
def libros(request):
    libros = Libro.objects.all()
    return render(request,'libros.html', {'libros': libros})
def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, '¡Libro Agregado!')   
        return redirect('libros')
    return render(request,'crear.html', {'formulario': formulario})
def editar(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        formulario = LibroForm(request.POST, request.FILES, instance=libro)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, '¡Libro Editado!')
            return redirect('libros')
    else:
        formulario = LibroForm(instance=libro)

    return render(request, 'editar.html', {'formulario': formulario, 'libro': libro})
def acerca(request):
    return render(request,'acerca.html')
def eliminar(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete(using=None, keep_parents=False)
    messages.error(request,"Libro Eliminado!")
    return redirect('libros')