from django.contrib import admin
from apps.investment_type.models import InvestmentType

# Register your models here.
class InvestmentTypeAdmin(admin.ModelAdmin):

    list_display = ('id','short_name', 'full_name','description')
    search_fields = ['short_name', 'full_name']

admin.site.register(InvestmentType, InvestmentTypeAdmin)