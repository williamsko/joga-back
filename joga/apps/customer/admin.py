from django.contrib import admin
from apps.customer.models import Customer, Proofs, ProofType

class CustomerAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'phone_number', 'country', 'address', )
    search_fields = ['user__first_name']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Proofs)
admin.site.register(ProofType)
