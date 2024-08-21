from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    fecha_ingreso = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.nombre_usuario


# Create your models here.
