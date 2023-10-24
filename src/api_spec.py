from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

spec = APISpec(
    title="Flask Application",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

class InputSchema(Schema):
    mac_address = fields.String(description="MAC address of the computer", required=True)

class OutputSchema(Schema):
    message = fields.String(description="Status message")

class ErrorSchema(Schema):
    message = fields.String(description="Status message")

spec.components.schema("Input", schema=InputSchema)
spec.components.schema("Output", schema=OutputSchema)

tags = [
            {"name": "wake on lan",
             "description": "Function for turning on a computer using wake on lan feature"
            },
       ]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)