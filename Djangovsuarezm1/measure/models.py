# Create your models here.

from django.db import models
import uuid
class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo =  models.CharField(verbose_name ='codigo', max_length=40, default ='1')
    nombre =  models.CharField(verbose_name ='nombre', max_length=40, default ='1')
    descripcion =  models.CharField(verbose_name ='descripcion', max_length=40, default ='1')
    tipoIndicador =  models.CharField(verbose_name ='tipoIndicador', max_length=40, default ='1')
    prioridad =  models.CharField(verbose_name ='prioridad', max_length=40, default ='1')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
