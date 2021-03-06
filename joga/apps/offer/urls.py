from django.urls import path
from django.conf.urls import url, include
from tastypie.api import Api
from apps.offer.api import OfferResource

v1_api = Api(api_name='v1')
v1_api.register(OfferResource())

urlpatterns = [url(r'^api/', include(v1_api.urls))]