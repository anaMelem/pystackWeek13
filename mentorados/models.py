from django.db import models
from django.contrib.auth.models import User

class Navigators(models.Model):
    nome = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #mentor

    def __str__(self):
        return self.nome
    
# Create your models here.
class Mentorados(models.Model):
    estagio_choices=(
        ('E1','10-100K'),
        ('E2', '100-1KK')
    )
    nome = models.CharField( max_length=255)    
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    navigator = models.ForeignKey(Navigators, null=True, on_delete=models.CASCADE)
    estagio = models.CharField( max_length=2, choices=estagio_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)#mentor
    criado_em= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome