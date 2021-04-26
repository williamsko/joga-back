from marshmallow import Schema, fields


class CustomerValidator(Schema):
    full_name = fields.Str(required=True)
    phone_number = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class CustomerLoginValidator(Schema):
    phone_number = fields.Str(required=True)
    password = fields.Str(required=True)
