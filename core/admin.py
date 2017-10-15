from django.contrib import admin
from sysOS.core.models import Customer, Address
from sysOS.workshop.models import JobType, Job


# Register your models here.
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(JobType)
admin.site.register(Job)