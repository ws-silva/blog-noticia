from django.db import models

# Create your models here.

class Noticia(models.Model):
    CATEGORIA_CHOICE= [
        ('DT', 'Destaque'),
        ('PA', 'Padrao'),
        ('SE', 'Semanal')
    ]
    titulo = models.CharField(max_length=250)
    sub_titulo = models.CharField(max_length=350)
    info = models.TextField()
    categoria = models.CharField(max_length=15, choices=CATEGORIA_CHOICE)
    img = models.ImageField('foto', upload_to ="")
    
    def __str__(self):
        return self.titulo