from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now())

    def __str__(self): #irá retornar o título do post no django admin. Quando for adicionado um Post.
        return self.titulo

