from django.shortcuts import render, redirect, get_object_or_404
from sysOS.workshop.forms import *
from sysOS.workshop.models import *

def add(request):
	job_form = JobForm()
	job_type_form = JobTypeForm()

	context = {
		'job_form': job_form,
		'job_type_form': job_type_form
	}

	return render(request, 'job/add.html', context)
