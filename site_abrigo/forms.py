'''
Classe do formulario => define quais campos vamos validar.
Field => campo do formulário, isto é, qual é o tipo do campo (senha, e-mail, nome, etc).
Widget => como o campo vai ser representado em HTML (input, text area, etc.)
'''
from django import forms

from .models  import CadastroAnimal

class FormCadastroAnimal(forms.ModelForm):
    class Meta:
        model = CadastroAnimal
        fields = ['nome', 'idade', 'raca', 'sexo', 'especie', 'historico_saude']
        exclude = ['data_criacao', 'disponivel']

        def __init__(self, *args, **kwargs):
            super(CadastroAnimal, self).__init__(*args, **kwargs)
            self.fields['nome'].widget.attrs.update({'placeholder': 'Nome do bichinho'})
            self.fields['idade'].widget.attrs.update({'placeholder': 'Digite a idade'})
            self.fields['historico_saude'].widget.attrs.update({'placeholder': 'Digite o historico de saude do animal'})
            self.fields['raca'].empty_label = "Selecione a raça" 
            self.fields['sexo'].empty_label = "Selecione o sexo" 
            self.fields['especie'].empty_label = "Selecione a espécie" 
