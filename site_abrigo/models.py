from django.db import models
import os

def upload_to(instance, CadastroAnimal):

    if isinstance(instance, CadastroAnimal):
        # Use instance.id to get the unique ID after the instance is saved
        if instance.id:
            return os.path.join('imagens', instance.nome, f'{instance.id}_{instance.nome.lower()}')
        else:
            return os.path.join('imagens', instance.nome, instance.nome)  # Para o caso em que o ID ainda não está disponível

    else:
        return os.path.join('imagens', instance.animal.nome, f'{instance.id}_{instance.animal.nome.lower()}') 

class CadastroAnimal(models.Model):
    SEXO = (('femea', 'Fêmea'), ('macho', 'Macho'),)
    ESPECIES = (('cachorro', 'Cachorro'), ('gato', 'Gato'), ('outros', 'Outros'),)

    nome = models.CharField(max_length=80)
    idade = models.IntegerField() 
    filhote = models.BooleanField(default=False)
    sexo = models.CharField(max_length=5, choices=SEXO)
    raca = models.CharField(null=True, blank=True, default='Viralata', max_length=80)
    especie = models.CharField(null=False, blank=False, max_length=8, choices=ESPECIES)
    data_criacao = models.DateTimeField(auto_now_add=True)
    disponivel_para_adocao = models.BooleanField(default=True)
        

    def __str__(self):
        # Retornando uma string que representa o animal
        return f'{self.nome} - {self.raca} ({self.especie})'
    

class GaleriaImagem(models.Model):
    animal = models.ForeignKey(CadastroAnimal,  related_name='galeria', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return f'Imagem de {self.cadastro_animal.nome}'