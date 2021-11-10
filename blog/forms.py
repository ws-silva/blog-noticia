from django import forms
from django.db.models import fields
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'sub_titulo', 'info', 'categoria', 'img']