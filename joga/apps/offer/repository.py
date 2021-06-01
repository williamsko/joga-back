from apps.offer.models import Offer

def retrieve_offer_by_identifier(id: str):
    return Offer.objects.get(id=id)

def create_offer(name,description,country,type,initial_amount,interest,maximum_amount,minimum_monthly_amount,maximum_monthly_amount,minimum_duration,maximum_duration,tax_value,
            tax_details,customer_conditions,financial_institution, is_active) -> Offer:
    offer.name = name,
    offer.description = description,
    offer.country = country,
    offer.type = type,
    offer.initial_amount = initial_amount,
    offer.interest = interest,
    offer.maximum_amount = maximum_amount,
    offer.minimum_monthly_amount = minimum_monthly_amount,
    offer.maximum_monthly_amount = maximum_monthly_amount,
    offer.minimum_duration = minimum_duration,
    offer.maximum_duration = maximum_duration,
    offer.tax_value = tax_value,
    offer.tax_details = tax_details,
    offer.customer_conditions = customer_conditions,
    offer.financial_institution = financial_institution,
    offer.is_active = is_active

    offer.save()
    return offer

def get_all_offers():
    return Offer.objects.all()

def retrieve_offer_by_country(country:str):
    return Offer.objects.get(country=country)

def retrieve_offer_by_financial_institution(financial_institution:str):
    return Offer.objects.get(financial_institution=financial_institution)

def retrieve_offer_by_offer_type(type:str):
    return Offer.objects.get(type=type)