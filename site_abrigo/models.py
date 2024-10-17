from django.db import models
import os

def upload_to(instance, filename):
    # Use instance.id to get the unique ID after the instance is saved
    if instance.id:
        return os.path.join('imagens', instance.nome, f'{instance.id}_{filename}')
    else:
        return os.path.join('imagens', instance.nome, filename)  # Para o caso em que o ID ainda não está disponível

SEXO = (('femea', 'Fêmea'), ('macho', 'Macho'),)
ESPECIES = (('cachorro', 'Cachorro'), ('gato', 'Gato'), ('outros', 'Outros'),)

class CadastroAnimal(models.Model):
    nome = models.CharField(unique=False, null=False, blank=False, max_length=80)
    idade = models.IntegerField(null=False, blank=False) 
    sexo = models.CharField(null=False, max_length=5, choices=SEXO)
    raca = models.CharField(null=False, blank=True, default='Viralata', max_length=80)
    especie = models.CharField(null=False, blank=False, max_length=8, choices=ESPECIES)
    imagem = models.ImageField(upload_to=upload_to)
    data_criacao = models.DateTimeField(auto_now_add=True)
    disponivel_para_adocao = models.BooleanField(default=True)

    def __str__(self):
<<<<<<< Updated upstream
        return f'Nome: {self.nome} - Espécie: {self.get_especie_display()}'
=======
        return self.nome
>>>>>>> Stashed changes
    

