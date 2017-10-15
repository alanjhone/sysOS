from django.db import models
from localflavor.br.forms import BRStateSelect
from sysOS import utils


STATES_CHOICES = BRStateSelect().choices

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True, db_column="customer_id")
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nome')
    ident = models.CharField(max_length=20, null=True, blank=True, verbose_name='CPF/CNPJ')
    email = models.EmailField(max_length=200, null=False, blank=False, verbose_name='E-mail')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Telefone')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        pass
    
    @property
    def get_pretty_ident(self):
        return utils.format_cpf(self.ident)

    @property
    def get_pretty_phone(self):
        return utils.format_phone(self.phone)

    @models.permalink
    def get_edit_url(self):
        return 'core:edit', (), {
            'customer_id': self.pk,
        }

    @models.permalink
    def get_delete_url(self):
        return 'core:delete', (), {
            'customer_id': self.pk,
        }


class Address(models.Model):
    id = models.AutoField(primary_key=True, db_column="address_id")
    state = models.CharField(max_length=3, null=True, blank=True, verbose_name='UF', choices=STATES_CHOICES)
    city = models.CharField(max_length=60, null=True, blank=True, verbose_name='Cidade')
    neighborhood = models.CharField(max_length=60, null=True, blank=True, verbose_name='Bairro')
    zipcode = models.CharField(max_length=9, null=True, blank=True, verbose_name='CEP')
    street = models.CharField(max_length=150, null=True, blank=True, verbose_name='Rua')
    complement = models.CharField(max_length=150, null=True, blank=True, verbose_name='Complemento')
    number = models.CharField(max_length=10, null=True, blank=True, verbose_name=u'Número')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    # relations
    customer = models.ForeignKey(Customer, null=False, blank=False, related_name="addresses", on_delete=models.CASCADE)

    @property
    def get_pretty_zipcode(self):
        return utils.format_zipcode(self.zipcode)

    @models.permalink
    def get_edit_url(self):
        return 'address_edit', (), {
            'address_id': self.pk,
        }

    @models.permalink
    def get_delete_url(self):
        return 'address_delete', (), {
            'address_id': self.pk,
            'customer_id': self.customer.id,
        }