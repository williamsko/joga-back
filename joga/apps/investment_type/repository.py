from apps.investment_type.models import InvestmentType

def retrieve_investment_type_by_identifier(id: str):
    return Bank.objects.get(id=id)

def create_investment_type(short_name, full_name, description) -> InvestmentType:
    investment_type = InvestmentType()
    investment_type.short_name = short_name
    investment_type.full_name = full_name
    investment_type.description = description

    investment_type.save()
    return investment_type

def get_all_investment_types():
    return InvestmentType.objects.all()