from marshmallow import Schema, fields

class InvestmentTypeValidator(Schema):
    short_name = fields.Str(required=True)
    full_name = fields.Str(required=False) # models.Choices()  # Have a table with a list of offer type to link it to
    description = fields.Str(required=False)