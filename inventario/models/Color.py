from django.db import models

class Color(models.Model):
    color = models.CharField(max_length = 50)
    codigo_hex = models.CharField(max_length = 7)
    
    def __str__(self):
        return self.color + " " + self.codigo_hex