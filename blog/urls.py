from django.urls import path

from . import views

urlpatterns = [
    path('', views.listaNoticias, name='lista-noticias'),
    path('myadmin', views.listaAdmin, name='lista-admin'),
    path('editar/<int:id>', views.editarNoticia, name='editar-noticia'),
    path('nova/', views.novaNoticia, name='nova-noticia'),
    path('delete/<int:id>', views.deleteNoticia, name='delete-noticia'),
]
