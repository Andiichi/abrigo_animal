from django import forms
from .models import CadastroAnimal

class FormCadastroDeAnimal(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = ['nome', 'idade','sexo','raca', 'especie', 'imagem', 'disponivel_para_adocao']
        labels = {
            'nome': 'Nome (apelido)',  # Alterando a label do campo 'nome'
            'idade': 'Idade (em anos)',  # Alterando a label do campo 'idade'
            'sexo': 'Sexo',
            'raca': 'Raça',
            'especie': 'Espécie',
            'imagem': 'Insira uma foto bem bonita do bichinho',
            'disponivel_para_adocao': 'Está disponível para adoção?',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control', 'required': True}, 
                choices=[
                ('macho', 'Macho'),
                ('femea', 'Fêmea'),
            ]),
            'especie': forms.Select(attrs={'class': 'form-control', 'required': True}, 
                choices=[
                ('gato', 'Gato'),
                ('cachorro', 'Cachorro'),
                ('outros', 'Outros'),
            ]),
            'raca': forms.TextInput(attrs={'class': 'form-control'}),
            'disponivel_para_adocao': forms.CheckboxInput(attrs={'class': 'form-check-input', "required": True}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'onchange': 'previewImage(event)'}),

        }
