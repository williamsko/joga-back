from django.urls import path
from django.conf.urls import include, url
from tastypie.api import Api
from apps.investment_type.api import InvestmentTypeResource

v1_api = Api(api_name='v1')
v1_api.register(InvestmentTypeResource())

urlpatterns = [url(r'^api/', include(v1_api.urls))]