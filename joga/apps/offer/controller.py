from apps.offer.validator import OfferValidator
from marshmallow import ValidationError
from apps.offer import repository as offer_repository
from apps.utils.exceptions import OfferException, PayloadException, \
    InternalException
from apps.offer.models import Offer
offer_validator = OfferValidator()

def new_offer(payload):
    _validate_offer_creation_payload(payload)
    name = payload.get('name')
    type = payload.get('type')
    initial_amount = payload.get('initial_amount')

    try:
        offer_repository.retrieve_offer_by_identifier(identifier)
        raise OfferException('Cette offre existe déjà')
    except exception:
        pass

    offer = offer_repository.create_offer(name,type,initial_amount)
    return {'identifier': offer.id}

def get_offer_by_identifier(identifier):
    try:
        return offer_repository.retrieve_offer_by_identifier(identifier)
    except Offer.DoesNotExist:
        raise OfferException('Offer nor found')

def get_all_offers():
    return offer_repository.get_all_offers()

def get_all_offers_by_country(country):
    try:
        return offer_repository.retrieve_offer_by_country(country)
    except Offer.DoesNotExist:
        raise OfferException('Offre introuvable')

def get_all_offers_by_financial_institution(financial_institution):
    try:
        return offer_repository.retrieve_offer_by_financial_institution(financial_institution)
    except Offer.DoesNotExist:
        raise OfferException('Offre introuvable')

def get_all_offers_by_offer_type(type):
    try:
        return offer_repository.retrieve_offer_by_offer_type(type)
    except Offer.DoesNotExist:
        raise OfferException('Offre introuvable')

def _validate_offer_creation_payload(payload):
    try:
        offer_validator.load(payload)
    except ValidationError as e:
        raise PayloadException(str(e))