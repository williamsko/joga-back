from apps.entity.models import FinancialInstitution

def retrieve_financial_institution_by_identifier(id: str):
    return FinancialInstitution.objects.get(id=id)

def create_financial_institution(short_name, full_name, type_of_financial_institution, code, street_address, city, postal_code, country) -> FinancialInstitution:

    financial_institution = FinancialInstitution()
    financial_institution.short_name = short_name
    financial_institution.full_name = full_name
    financial_institution.code = code
    financial_institution.type_of_financial_institution = type_of_financial_institution
    financial_institution.street_address = street_address
    financial_institution.city = city
    financial_institution.postal_code = postal_code
    financial_institution.country = country

    financial_institution.save()

    return financial_institution

def get_all_financial_institutions():
    return FinancialInstitution.objects.all()

def retrieve_financial_institution_by_country(country:str):
    return FinancialInstitution.objects.get(country=country)

def retrieve_financial_institution_by_code(code:str):
    return FinancialInstitution.objects.get(code=code)