from django.http import request
from django.shortcuts import render, redirect
from .models import Noticia
from .forms import NoticiaForm
import somewhere
# Create your views here.

def listaNoticias(request):
    noticias_dt = Noticia.objects.filter(categoria='DT')
    noticias_pa = Noticia.objects.filter(categoria='PA')
    noticias_se = Noticia.objects.filter(categoria='SE')
    return render (request, 'noticia.html', {'noticias_dt': noticias_dt, 
                                            'noticias_pa': noticias_pa, 
                                            'noticias_se': noticias_se})


def listaAdmin(request):
    noticias_dt = Noticia.objects.filter(categoria='DT')
    noticias_pa = Noticia.objects.filter(categoria='PA')
    noticias_se = Noticia.objects.filter(categoria='SE')
    return render (request, 'myadmin.html', {'noticias_dt': noticias_dt, 
                                            'noticias_pa': noticias_pa, 
                                            'noticias_se': noticias_se})

def editarNoticia(request, id):
    noticia = Noticia.objects.get(id=id)
    form = NoticiaForm(instance=noticia)
    if (request.method) == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect ('/myadmin')
        else:
            return render(request, 'editnoticia.html', {'form': form})
    return render(request, 'editnoticia.html', {'form': form, 'noticia': noticia})

def novaNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/myadmin')
    else:
        form = NoticiaForm()
    return render(request, 'new.html', {'form':form})

def deleteNoticia(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()
    return redirect('/myadmin')