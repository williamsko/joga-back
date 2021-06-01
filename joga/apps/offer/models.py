from django.db import models
from apps.investment_type.models import InvestmentType
from apps.entity.models import FinancialInstitution
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from .constants import DEFAULT_CURRENCY
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

# Create your models here.
class Offer(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000,blank=True,null=True)
    country = CountryField()
    type = models.ForeignKey(InvestmentType,on_delete=models.SET_NULL, blank=True,null=True)
    initial_amount = MoneyField(max_digits=14, decimal_places=2, default_currency=DEFAULT_CURRENCY)
    interest = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        decimal_places=2,
        max_digits=5,
        help_text='Interest rate from 0 - 100'
    )
    maximum_amount = MoneyField(max_digits=14, decimal_places=2, default_currency=DEFAULT_CURRENCY, null=True)
    minimum_monthly_amount = MoneyField(max_digits=14, decimal_places=2, default_currency=DEFAULT_CURRENCY)
    maximum_monthly_amount = MoneyField(max_digits=14, decimal_places=2, default_currency=DEFAULT_CURRENCY,null=True)
    minimum_duration = models.DurationField()
    maximum_duration = models.DurationField(null=True)
    tax_value = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        decimal_places=2,
        max_digits=5,
        help_text='Country tax rate from 0 - 100',
        null=True
    )
    tax_details = models.CharField(max_length=200,blank=True,null=True)
    customer_conditions = models.CharField(max_length=200,blank=True,null=True)
    financial_institution = models.ForeignKey(FinancialInstitution,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')
        app_label = 'offer'