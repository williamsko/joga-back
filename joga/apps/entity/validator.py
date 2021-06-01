from marshmallow import Schema, fields

class FinancialInstitutionValidator(Schema):
    short_name = fields.Str(required=True)
    full_name = fields.Str(required=False)
    country = fields.Str(required=True)