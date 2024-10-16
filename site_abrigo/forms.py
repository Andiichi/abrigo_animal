from django import forms
from .models import CadastroAnimal

class FormCadastroDeAnimal(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = ['nome', 'idade','sexo','raca', 'especie', 'disponivel_para_adocao', 'imagem']
        labels = {
            'nome': 'Nome (apelido)',  # Alterando a label do campo 'nome'
            'idade': 'Idade (em anos)',  # Alterando a label do campo 'idade'
            'sexo': 'Sexo',
            'raca': 'Raça',
            'especie': 'Espécie',
            'disponivel_para_adocao': 'Está disponível para adoção?',
            'imagem': 'Insira uma foto bem bonita do bichinho',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', "required": True}),
            'idade': forms.NumberInput(attrs={'class': 'form-control'}),
            'especie': forms.Select(attrs={"required": True}),
            'raca': forms.TextInput(attrs={'class': 'form-control'}),
            'disponivel_para_adocao': forms.CheckboxInput(attrs={'class': 'form-check-input', "required": True}),

        }