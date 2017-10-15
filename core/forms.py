from django import forms
from .models import *

class AddressForm(forms.ModelForm):
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
        'placeholder': 'Cep', 'data-mask': 'zipcode'}), required=False)

    class Meta:
        model = Address
        exclude = ['customer']
        fields = ['city', 'state', 'zipcode', 'complement', 'neighborhood', 'street', 'number']
        widgets = {
            'state': forms.Select(attrs={'data-placeholder': u'Escolha seu estado.', 'class': 'form-control'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'complement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Complemento'}),
            'street': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Rua'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'})
        }

    def clean_zipcode(self):
        if self.cleaned_data.get('zipcode'):
            return self.cleaned_data.get('zipcode').replace('-','')


AddressInlineFormSet = forms.models.inlineformset_factory(Customer, Address, form=AddressForm, extra=1, can_delete=False)

class CustomerForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Ex.: admin@admin.com'})
    )

    class Meta:
        model = Customer
        fields = ['name', 'ident', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            # FIXME: colocar máscara dinamicamente
            'ident': forms.TextInput(attrs={'data-mask': 'cpf', 'class': 'form-control', 'placeholder': 'Ex.: 111.111.111-11'}),
            'phone': forms.TextInput(attrs={'maxlength': 15, 'data-mask': 'phone', 'class': 'form-control', 'placeholder': 'Ex.: 99999-999'}),
        }

    def clean_ident(self):
        if self.cleaned_data.get('ident'):
           return (self.cleaned_data.get('ident').replace('.', '')).replace('-','')

    def clean_phone(self):
        if self.cleaned_data.get('phone'):
            return (((self.cleaned_data.get('phone').replace('-', '')).replace('(','')).replace(')','')).replace(' ','')
