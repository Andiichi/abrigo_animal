from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CadastroAnimal


class CadastroAnimalAdmin(admin.ModelAdmin):
    list_display = ['nome',  'especie', 'data_criacao']  # Campos a serem exibidos na lista
    search_fields = ['nome', 'raca']  # Campos que podem ser pesquisados
    list_filter = ['especie', 'sexo', 'disponivel_para_adocao']  # Filtros disponíveis na barra lateral

    # Exibir imagem no admin
    def image_tag(self, obj):
        if obj.imagem:
            return mark_safe(f'<img src="{obj.imagem.url}" style="width: 100px; height: auto;" />')
        return "No image"
    image_tag.short_description = 'Imagem'

    # Incluir a imagem na lista
    list_display += ['image_tag', 'disponivel_para_adocao']


admin.site.register(CadastroAnimal, CadastroAnimalAdmin)