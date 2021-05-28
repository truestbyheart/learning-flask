from marshmallow import Schema, fields

class RegisterSchema(Schema):
    """
    endpoint: /auth/register
    parameters:
        full_name: string,
        username: string,
        password: string,
        email: string
    """
    full_name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)
