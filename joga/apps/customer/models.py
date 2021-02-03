from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        app_label = 'customer'

class ProofType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    short_name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.short_name}'

    class Meta:
        verbose_name = _('Proof type')
        verbose_name_plural = _('Poofs type')
        app_label = 'customer'


class ProofContent(models.Model):
    file = models.FileField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        app_label = 'customer'

class Proofs(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.DO_NOTHING, null=False, blank=False)
    type = models.ForeignKey('ProofType', on_delete=models.DO_NOTHING, null=False, blank=False)
    content = models.ManyToManyField('ProofContent', null=False, blank=False)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Proof')
        verbose_name_plural = _('Proofs')
        app_label = 'customer'
