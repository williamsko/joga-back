from tastypie.resources import ModelResource, ALL
from django.conf.urls import url
from tastypie.utils import trailing_slash
from apps.entity import controller as financial_institution_controller
from apps.utils.exceptions import FinancialInstitutionException
from tastypie.http import HttpUnauthorized, HttpForbidden,\
    HttpCreated, HttpApplicationError, HttpConflict
from tastypie.authorization import Authorization
from marshmallow import ValidationError

API_FORMAT = 'application/json'

class FinancialInstitutionResource(ModelResource):
    class Meta:
        queryset = financial_institution_controller.get_all_financial_institutions()
        fields = []  ## here, this doesn't work as intended
        list_allowed_methods = ['get','post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'financial_institution'
        filtering = {
            'slug': ALL,
            'identifier': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()

    def dehydrate(self, bundle):
        bundle.data['short_name'] = bundle.obj.short_name
        bundle.data['full_name'] = bundle.obj.full_name
        bundle.data['country'] = bundle.obj.country
        bundle.data['code'] = bundle.obj.code
        bundle.data['type_of_financial_institution'] = bundle.obj.type_of_financial_institution
        bundle.data['city'] = bundle.obj.city
        return bundle

    def determine_format(self, request):
        return API_FORMAT

    def prepend_urls(self):
        return []