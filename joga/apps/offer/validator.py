from marshmallow import Schema, fields

class OfferValidator(Schema):
    name = fields.Str(required=True)
    type = fields.Int(required=True) # models.Choices()  # Have a table with a list of offer type to link it to
    initial_amount = fields.Float(required=True)
    financial_institution = fields.Int(required=True)