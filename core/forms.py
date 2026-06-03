from django import forms
from .models import Cliente, Pet, Servico, Agendamento

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(ativo=True)


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = '__all__'

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {

            'nome': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do cliente'
            }),

            'telefone': forms.TextInput(attrs={
                'placeholder': '(83) 99999-9999'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'email@gmail.com'
            }),

            'endereco': forms.TextInput(attrs={
                'placeholder': 'Rua, número, bairro...'
            }),
        }