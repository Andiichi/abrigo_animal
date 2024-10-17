from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.utils.translation import ngettext
from .models import CadastroAnimal

# Admin Site configurações
admin.sites.AdminSite.site_header = 'Site Abrigo Animal'
admin.sites.AdminSite.site_title = 'Abrigo Animal'
admin.sites.AdminSite.index_title = 'Admin Abrigo Animal'

class CadastroAnimalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'especie', 'data_criacao', 'sexo']  # Campos a serem exibidos na lista
    search_fields = ['nome', 'raca']  # Campos que podem ser pesquisados
    list_filter = ['especie', 'sexo', 'disponivel_para_adocao']  # Filtros disponíveis na barra lateral
    ordering = ['nome']  # Ordenação por nome

    # Exibir imagem no admin
    def image_tag(self, obj):
        if obj.imagem:
            return mark_safe(f'<img src="{obj.imagem.url}" style="width: 100px; height: auto;" />')
        return "Sem imagem"
    
    image_tag.short_description = 'Imagem'

    # Campo customizado para adoção
    def adocao_tag(self, obj):
        return obj.disponivel_para_adocao
    
    adocao_tag.boolean = True
    adocao_tag.short_description = 'Disponível para adoção'

    # Incluir a imagem e disponibilidade para adoção na lista
    list_display += ['image_tag', 'adocao_tag']

    # Ação personalizada para alterar o sexo para 'fêmea'
    @admin.action(description="Alterar sexo para Fêmea")
    def marcar_como_femea(self, request, queryset):

        # Altera apenas os animais que atualmente estão marcados como 'macho'
        machos = queryset.filter(sexo="macho")
        updated = machos.update(sexo="femea")
        
        # Exibir mensagem de confirmação
        self.message_user(
            request,
            ngettext(
                "%d animal marcado como 'Fêmea'.",
                "%d animais marcados como 'Fêmea'.",
                updated,
            ) % updated,
            messages.SUCCESS,
        )


     # Ação personalizada para alterar o sexo para 'macho'
    @admin.action(description="Alterar sexo para Macho")
    def marcar_como_macho(self, request, queryset):

        # Altera apenas os animais que atualmente estão marcados como 'femea'
        machos = queryset.filter(sexo="femea")
        updated = machos.update(sexo="macho")
        
        # Exibir mensagem de confirmação
        self.message_user(
            request,
            ngettext(
                "%d animal marcado como 'Macho'.",
                "%d animais marcados como 'Macho'.",
                updated,
            ) % updated,
            messages.SUCCESS,
        )

    actions = [marcar_como_macho, marcar_como_femea]

admin.site.register(CadastroAnimal, CadastroAnimalAdmin)
