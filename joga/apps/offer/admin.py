from django.contrib import admin
from apps.offer.models import Offer

class OfferAdmin(admin.ModelAdmin):

    list_display = ('id','name', 'country', 'type', 'interest')
    search_fields = ['name', 'type', 'country', 'interest']

admin.site.register(Offer, OfferAdmin)