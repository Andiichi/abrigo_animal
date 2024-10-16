from django.db import models
import os


def upload_to(instance, filename):
    # Use instance.id to get the unique ID after the instance is saved
    if instance.id:
        return os.path.join('imagens', instance.nome, f'{instance.id}_{filename}')
    else:
        return os.path.join('imagens', instance.nome, filename)  # Para o caso em que o ID ainda não está disponível
    
class CadastroAnimal(models.Model):
    ESPECIES = (
        ('1', 'Cachorro'),
        ('2', 'Gato'),
        ('3', 'Outros'),
    )

    SEXO = (
        ('F', 'Fêmea'),
        ('M', 'Macho'),
    )

    nome = models.CharField(unique=False, null=False, blank=False, max_length=80)
    idade = models.IntegerField(null=False, blank=False) 
    sexo = models.CharField(null=False, blank=False, max_length=1, choices=SEXO)
    raca = models.CharField(unique=False, null=True, blank=True, default='Viralata', max_length=80)
    especie = models.CharField(null=False, blank=False, max_length=1, choices=ESPECIES)
    imagens = models.ImageField(upload_to=upload_to, null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    disponivel_para_adocao = models.BooleanField(default=True)


    def __str__(self):
        return f'Nome: {self.nome} - Espécie: {self.especie}'
    

    