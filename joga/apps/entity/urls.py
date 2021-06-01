from django.urls import path
from django.conf.urls import include, url
from tastypie.api import Api
from apps.entity.api import FinancialInstitutionResource

v1_api = Api(api_name='v1')
v1_api.register(FinancialInstitutionResource())

urlpatterns = [url(r'^api/', include(v1_api.urls))]