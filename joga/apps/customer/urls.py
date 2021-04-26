from django.urls import path
from django.conf.urls import include
from tastypie.api import Api

v1_api = Api(api_name='api')

urlpatterns = [
    path('', include(v1_api.urls)),
]
