""" Imports """
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin


# Create an APISpec
spec = APISpec(
    title="ipp-fleet-management-api",
    version="1.0.3",
    openapi_version="3.0.3",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
    info={
        "description": "This is a API REST to query the locations of the vehicles of a taxi company in Beijing, China." # pylint: disable=line-too-long
    }
)

# Tags > Taxis
spec.tag(
    {
        "name": "taxis", 
        "description": "Taxi related operations" 
    }
)

# Tags > Trajectories
spec.tag(
    {
        "name": "trajectories", 
        "description": "Trajectories related operations" 
    }
)

# Components > Schemas > Taxi
spec.components.schema(
    "Taxi",
    {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "plate": {"type": "string"},
        }
    },
)

# Components > Schemas > Trajectorie
spec.components.schema(
    "Trajectorie",
    {
        "type": "object",
        "properties": {
            "taxi_id": {"type": "integer"},
            "date": {"type": "string", "format": "date-time"},
            "latitude": {"type": "number", "format": "double"},
            "longitude": {"type": "number", "format": "double"}
        }
    }
)


# Components > Responses 404
spec.components.response(
    "NotFound", {
        "description": "No information found"
    }
)

# Components > Responses 400
spec.components.response(
    "BadRequest", {
        "description": "The data sent is incorrect"
    }
)

# Components > Responses 500
spec.components.response(
    "ServerError", {
        "description": "Server error"
    }
)

# End-of-file
