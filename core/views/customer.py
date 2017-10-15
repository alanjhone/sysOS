from django.shortcuts import render, redirect, get_object_or_404
from sysOS.core.forms import *
from django.contrib import messages
from django.db import transaction
from django.views.generic.list import ListView
from sysOS.core.models import Address, Customer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def add(request):
	if request.method == 'POST':
		customer_form = CustomerForm(request.POST)
		address_form = AddressInlineFormSet(request.POST, prefix="nested")
		if customer_form.is_valid():
			with transaction.atomic():
				customer = customer_form.save(commit=False)
				address_form = AddressInlineFormSet(request.POST, instance=customer, prefix="nested")

				if address_form.is_valid():
					customer.save()
					address_form.save()
					
					messages.success(request, 'Cadastro Realizado com sucesso!')
					return redirect('core:list')
				else:
					messages.error(request, 'Não foi possível realizar o cadastro')
		else:
			messages.error(request, 'Não foi possível realizar o cadastro')

	else:
		customer_form = CustomerForm()
		address_form = AddressInlineFormSet(instance=Customer(), prefix="nested")

	context = {
		'customer_form': customer_form,
		'address_form': address_form,
	}
	
	return render(request, 'customer/add.html', context)

@method_decorator(login_required, name='dispatch')
class CustomerListView(ListView):
	model = Customer
	template_name = 'customer/list.html'
	context_object_name = 'customers'  # Default: object_list
	paginate_by = 5
	queryset = Customer.objects.all()  # Default: Model.objects.all()

@login_required
def edit(request, customer_id):
	customer = get_object_or_404(Customer, pk=customer_id)

	if request.method == 'POST':
		customer_form = CustomerForm(request.POST, instance=customer)
		address_form = AddressInlineFormSet(request.POST, instance=customer, prefix="nested")

		if customer_form.is_valid() and address_form.is_valid():			
			with transaction.atomic():
				customer_form.save()				
				address_form.save()

				messages.success(request, 'Dados atualizados com sucesso!')
				return redirect('core:list')
		else:
			messages.error(request, 'Não foi possível atualizar o cadastro!')

	else:
		customer_form = CustomerForm(instance=customer)
		address_form = AddressInlineFormSet(instance=customer, prefix="nested")

	context = {
		'customer_form':  customer_form,
		'address_form': address_form,
	}
	
	return render(request, 'customer/edit.html', context)

@login_required
def delete(request, customer_id):
	customer = get_object_or_404(Customer, pk=customer_id)
	customer.delete()
	return redirect('core:list')