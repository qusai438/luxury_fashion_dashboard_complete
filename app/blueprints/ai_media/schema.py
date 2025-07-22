from marshmallow import Schema, fields, ValidationError

class ImageGenerationRequestSchema(Schema):
    image_data = fields.String(required=True)  # base64 image string
    style = fields.String(required=False)      # optional: "luxury", "casual", etc.
    language = fields.String(missing="en")     # default to English
