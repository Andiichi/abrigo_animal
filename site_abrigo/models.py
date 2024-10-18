from django.db import models
from django.utils.safestring import mark_safe

# Função que define onde o arquivo será salvo
def upload_to(instance, filename):
    # Verifica se o nome está presente para evitar erro ao salvar a imagem
    nome_animal = instance.nome if hasattr(instance, 'nome') and instance.nome else instance.id
    return f'imagens/{nome_animal}/{filename}'


class CadastroAnimal(models.Model):
    SEXO = (
        ('femea', 'Fêmea'),
        ('macho', 'Macho'),
    )
    ESPECIES = (
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('outros', 'Outros'),
    )

    nome = models.CharField(unique=False, null=False, blank=False, max_length=80)
    idade = models.IntegerField(null=False, blank=False)
    sexo = models.CharField(null=False, max_length=5, choices=SEXO)
    raca = models.CharField(null=False, blank=True, default='Viralata', max_length=80)
    especie = models.CharField(null=False, blank=False, max_length=8, choices=ESPECIES)
    imagem = models.ImageField(upload_to=upload_to)
    data_criacao = models.DateTimeField(auto_now_add=True)
    disponivel_para_adocao = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Cadastro de Animal'
        verbose_name_plural = 'Cadastro de Animais'
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
     # Exibir a imagem no admin
    def image_tag(self):
        if self.imagem:
            return mark_safe(f'<img src="{self.imagem.url}" style="width: 100px; height: auto;" />')
        return "Sem imagem"

    image_tag.short_description = 'Imagem'

class GaleriaImagem(models.Model):
    animal = models.ForeignKey(CadastroAnimal, on_delete=models.CASCADE, related_name='galeria')
    imagem = models.ImageField(upload_to=upload_to)

    class Meta:
        verbose_name = 'Imagem da Galeria'
        verbose_name_plural = 'Imagens da Galeria'

    def __str__(self):
        return f'Imagem de {self.animal.nome}'

    # Exibir a imagem no admin
    def image_tag(self):
        if self.imagem:
            return mark_safe(f'<img src="{self.imagem.url}" style="width: 100px; height: auto;" />')
        return "Sem imagem"

    image_tag.short_description = 'Imagem'
