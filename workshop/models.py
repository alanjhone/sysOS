from django.db import models
from sysOS import utils

# Create your models here.

class JobType(models.Model):
	id = models.AutoField(primary_key=True, db_column="job_type_id")
	name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nome')
	slug_name = models.SlugField(max_length=200, unique=True)
	description = models.CharField(max_length=15000, null=True, blank=True, verbose_name='Descrição')

	def save(self, *args, **kwargs):
		if not self.slug_name:
			self.slug_name = utils.slugfy_data(self.name)
		super.save()

class Job(models.Model):
	id = models.AutoField(primary_key=True, db_column="job_id")
	description = models.CharField(max_length=15000, null=True, blank=True, verbose_name='Descrição')
	value = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, default=0, verbose_name='Valor')

	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)


	# relations
	job_type = models.ForeignKey(JobType, null=False, blank=False, related_name="job_type", on_delete=models.CASCADE, verbose_name='Tipo')
