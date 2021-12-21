from django import forms

conforto_seq = {
    ('A', 'Alto conforto'),
    ('M', 'Médio conforto'),
    ('C', 'Conforto comercial'),
}

class OnibusForms(forms.Form):
    ponto_a = forms.CharField(label="Origem", max_length=140)
    ponto_b = forms.CharField(label="Destino", max_length=140)
    dia_de_ida = forms.DateField(label='Data da ida')
    dia_de_volta = forms.DateField(label='Retorno')
    conforto = forms.ChoiceField(label='Conforto', choices=conforto_seq)

# Essa função de validação DEVE começar com a palavra 'clean_' e depois deve ser inserido o nome do campo do form.
    def clean_ponto_a(self):
        ponto_a = self.cleaned_data.get('ponto_a')
        if any(char.isdigit() for char in ponto_a):
            raise forms.ValidationError('Apenas letras, por favor.')
        else:
            return ponto_a

    def clean_ponto_b(self):
        ponto_b = self.cleaned_data.get('ponto_b')
        if any(char.isdigit() for char in ponto_b):
            raise forms.ValidationError('Apenas letras, por favor.')
        else:
            return ponto_b

    def clean(self):
        ponto_a = self.cleaned_data.get('ponto_a')
        ponto_b = self.cleaned_data.get('ponto_b')
        if ponto_a == ponto_b:
            self.add_error('ponto_b', 'Origem e destino devem ser diferentes.')