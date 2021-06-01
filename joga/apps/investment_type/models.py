from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class InvestmentType(models.Model):
    short_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _('Investment type')
        verbose_name_plural = _('Investments type')
        app_label = 'investment_type'