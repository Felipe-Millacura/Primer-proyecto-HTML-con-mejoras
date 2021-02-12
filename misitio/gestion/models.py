from django.db import models

# Create your models here.

ESTADOSS = (('Rescatado',"Rescatado"), ('Disponible','Disponible'),('Adoptado','Adoptado')) 

class perrito(models.Model):
    Foto= models.ImageField(upload_to='Media',blank=True,null=True)
    Nombre = models.CharField(max_length=100)
    Raza = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=1000)
    Estado = models.CharField(max_length = 11, choices = ESTADOSS, default = 'Rescatado')

    def __str__(self):
        return self.Nombre

class user(models.Model):
    Email = models.EmailField(max_length=100)
    Nombre = models.CharField(max_length=100)
    FechaNacimiento = models.DateField()
    Telefono = models.CharField(max_length=9)
    Usuario = models.CharField(max_length=100)
    Clave = models.CharField(max_length=100)
    Rut = models.CharField(max_length=12)

    def __str__(self):
        return self.Nombre
