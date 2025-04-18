from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
import secrets
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
    token =  models.CharField(max_length=16)

    def save(self,*args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(8)
        super().save(*args, **kwargs )
        
    def gerar_token_unico(self):
        while True:
            token = secrets.token_urlsafe(8)
            if not Mentorados.objects.filter(token=token).exists():
                return token
            

    def __str__(self):
        return self.nome
    
class DisponibilidadeHorarios(models.Model):
    data_inicial = models.DateTimeField(null=True, blank=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    agendado = models.BooleanField(default=False)

    def data_final (self):
        return self.data_inicial + timedelta(minutes=50)
