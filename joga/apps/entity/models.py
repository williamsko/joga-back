from django.db import models
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from .constants import INSTITUTIONS_TYPE_CHOICES
from django.utils.translation import ugettext_lazy as _

# Bank basic model
class FinancialInstitution(models.Model):
    short_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=2000, blank=True, null=True)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    type_of_financial_institution = models.CharField(max_length=30, choices=INSTITUTIONS_TYPE_CHOICES, default='')
    code = models.CharField(max_length=11, validators=[alphanumeric], unique=True)
    street_address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    postal_code = models.PositiveIntegerField()
    # TODO : Implement foreign key relation.
    # The code of the institution must be unique per country
    country = CountryField()

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _('FinancialInstitution')
        verbose_name_plural = _('FinancialInstitutions')