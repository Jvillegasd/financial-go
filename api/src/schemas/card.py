from marshmallow import fields
from src.schemas.base.library import MarshmallowSchema


class CardSchema(MarshmallowSchema):
    owner_id = fields.UUID()
    title = fields.String()
    initial_amount = fields.Float()
