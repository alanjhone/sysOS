from django.conf.urls import url
from .views import job

urlpatterns = [

	# jobs
	url(r'^add/$', job.add, name='add'),
]