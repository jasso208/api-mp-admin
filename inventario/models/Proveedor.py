from unittest.util import _MAX_LENGTH


from django.db import models

class Proveedor(models.Model):
    descripcion = models.CharField(max_length=50,null=False,blank=False)
    activo = models.CharField(max_length=1,default = "S",choices = [('S','S'),('N','N')])
    
    def save(self,*args,**kwargs):
        self.descripcion = self.descripcion.upper()
        return super(Proveedor,self).save(*args,**kwargs)

    def __str__(self):
        return self.descripcion
        