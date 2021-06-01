from apps.investment_type.validator import InvestmentTypeValidator
from marshmallow import ValidationError
from apps.investment_type import repository as investment_type_repository
from apps.utils.exceptions import BankException, PayloadException, \
    InternalException, InvestmentTypeException
from apps.investment_type.models import InvestmentType

investment_type_validator = InvestmentTypeValidator()

def new_investment_type(payload):
    _validate_investment_type_creation_payload(payload)
    short_name = payload.get('short_name')
    full_name = payload.get('full_name')
    description = payload.get('description')

    if InvestmentType.objects.filter(id=id).exists():
        raise ValidationError('This type of investment already exists in the system')
    else:
        investment_type = investment_type_repository.create_investment_type(short_name,full_name,description)

    return {'id': investment_type.id}

def get_investment_type_by_identifier(identifier):
    try:
        return investment_type_repository.retrieve_investment_type_by_identifier(identifier)
    except InvestmentType.DoesNotExist:
        raise InvestmentTypeException('Investment type not found')

def get_all_investment_types():
    return investment_type_repository.get_all_investment_types()


def _validate_investment_type_creation_payload(payload):
    try:
        investment_type_validator.load(payload)
    except ValidationError as e:
        raise PayloadException(str(e))