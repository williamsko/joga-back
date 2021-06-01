from django.contrib import admin
from apps.entity.models import FinancialInstitution

# Register your models here.
class FinancialInstitutionAdmin(admin.ModelAdmin):

    list_display = ('id', 'short_name', 'full_name', 'country', 'code')
    search_fields = ['short_name', 'full_name', 'country']

admin.site.register(FinancialInstitution, FinancialInstitutionAdmin)