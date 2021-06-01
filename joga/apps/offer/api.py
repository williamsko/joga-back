from tastypie.resources import ModelResource, ALL
from django.conf.urls import url
from tastypie.utils import trailing_slash
from apps.offer import controller as offer_controller
from apps.utils.exceptions import OfferException
from tastypie.http import HttpUnauthorized, HttpForbidden,\
    HttpCreated, HttpApplicationError, HttpConflict
from tastypie.authorization import Authorization
from marshmallow import ValidationError
from apps.utils.api import MultiPartResource

API_FORMAT = 'application/json'

class OfferResource(ModelResource):
    class Meta:
        queryset = offer_controller.get_all_offers()
        fields = []  ## here, this doesn't work as intended
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'offer'
        filtering = {
            'slug': ALL,
            'identifier': ALL,
            'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }
        authorization = Authorization()

    def dehydrate(self, bundle):
        bundle.data['name'] = bundle.obj.name
        bundle.data['type'] = bundle.obj.type
        bundle.data['initial_amount'] = bundle.obj.initial_amount.amount
        bundle.data['initial_amount_currency'] = bundle.obj.initial_amount.currency
        bundle.data['financial_institution'] = bundle.obj.financial_institution
        return bundle

    def determine_format(self, request):
        return API_FORMAT

    def prepend_urls(self):
        print(trailing_slash())
        return [
            url(r'^create%s$' % trailing_slash(), self.wrap_view(
                'create_new_offer'), name='api_create_new_offer')
        ]

    def create_new_offer(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        payload = self.deserialize(request, request.body)
        try:
            response = offer_controller.new_offer(payload)
        except OfferException as e:
            return self.create_response(
                request, {'error': str(e)}, HttpConflict)
        except Exception as e:
            return self.create_response(
                request, {'error': str(e)}, HttpApplicationError)

        except ValidationError as e:
            return self.create_response(
                request, {'error': str(e)}, HttpApplicationError)
        return self.create_response(request, response, HttpCreated)