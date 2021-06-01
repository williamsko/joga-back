from tastypie.resources import ModelResource, ALL
from django.conf.urls import url
from tastypie.utils import trailing_slash
from apps.investment_type import controller as investment_type_controller
from apps.utils.exceptions import InvestmentTypeException
from tastypie.http import HttpUnauthorized, HttpForbidden,\
    HttpCreated, HttpApplicationError, HttpConflict
from tastypie.authorization import Authorization
from marshmallow import ValidationError
from apps.utils.api import MultiPartResource

API_FORMAT = 'application/json'

class InvestmentTypeResource(ModelResource):
    class Meta:
        queryset = investment_type_controller.get_all_investment_types()
        fields = []  ## here, this doesn't work as intended
        list_allowed_methods = ['get','post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'investment_type'
        filtering = {
            'slug': ALL,
            'identifier': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()

    def determine_format(self, request):
        return API_FORMAT

    def prepend_urls(self):
        return []