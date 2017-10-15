from django import forms
from .models import *

class JobTypeForm(forms.ModelForm):
	class Meta:
		model = JobType
		fields = ['name', 'description']
		exclude = ['slug_name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
			'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control', 'style':'resize:none;'}),
		}

class JobForm(forms.ModelForm):

	job_type = forms.ModelChoiceField(
		queryset=JobType.objects.all(), empty_label="(Selecione um tipo de serviço)",
		widget=forms.Select(attrs={'class':'form-control'})
	)

	class Meta:
		model = Job
		fields = ['job_type', 'value', 'description']
		widgets = {
			'value': forms.NumberInput(attrs={'data-mask': 'monetary', 'class': 'form-control', 'placeholder': '0,00'}),
			'description': forms.Textarea(attrs={'rows': 10, 'class': 'form-control', 'style':'resize:none;'}),
		}