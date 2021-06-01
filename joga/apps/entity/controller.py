from apps.entity.validator import FinancialInstitutionValidator
from marshmallow import ValidationError
from apps.entity import repository as financial_institution_repository
from apps.utils.exceptions import FinancialInstitutionException, PayloadException, \
    InternalException
from apps.entity.models import FinancialInstitution

financial_institution_validator = FinancialInstitutionValidator()

def new_financial_institution(payload):
    _validate_financial_institution_creation_payload(payload)
    short_name = payload.get('short_name')
    full_name = payload.get('full_name')
    code = payload.get('code')
    type_of_financial_institution = payload.get('type_of_financial_institution')
    street_address = payload.get('street_address')
    city = payload.get('city')
    postal_code = payload.get('postal_code')
    country = payload.get('country')

    if FinancialInstitution.objects.filter(code=code).exists():
        raise ValidationError('The financial institution already exists in the system')
    else:
        financial_institution = financial_institution_repository.create_financial_institution(short_name, full_name, type_of_financial_institution, code, street_address, city, postal_code, country)

    return {'id': financial_institution.id}

def get_financial_institution_by_identifier(id):
    try:
        return financial_institution_repository.retrieve_financial_institution_by_id(id)
    except FinancialInstitution.DoesNotExist:
        raise FinancialInstitutionException('The financial institution is not found')

def get_all_financial_institutions():
    return financial_institution_repository.get_all_financial_institutions()

def get_all_financial_institution_by_country(country):
    try:
        return financial_institution_repository.retrieve_financial_institution_by_country(country)
    except FinancialInstitution.DoesNotExist:
        raise FinancialInstitutionException('The financial institution is not found')

def _validate_financial_institution_creation_payload(payload):
    try:
        financial_institution_validator.load(payload)
    except ValidationError as e:
        raise PayloadException(str(e))