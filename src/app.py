""" imports """
import psycopg2
from flask import Flask, json
from werkzeug.exceptions import HTTPException
from models.taxi import Taxis, Trajectories
from schemas.components import spec

app = Flask(__name__)

@app.route('/taxis', methods=['GET'])
def get_taxis():
    """ Get list of all taxis.
    ---
    get:
        tags:
            - taxis
        summary: Returns all taxis
        description: Returns all taxis (id, plate)
        responses:
            '200':
                description: OK - All the taxis were successfully brought
                content:
                    application/json:
                        schema:
                            type: array
                            items:
                                $ref: '#/components/schemas/Taxi'
            '404':
                $ref: '#/components/responses/NotFound'
            '500':
                $ref: '#/components/responses/ServerError'
    """
    try:
        return Taxis.get_taxis()
    except psycopg2.Error as ex:
        return str(ex)

@app.route('/trajectories/<taxi_id>/<date>', methods=['GET'])
def get_trajectories_for_id(taxi_id, date):
    """ Get all trajectories with id and only date 
    ---
    get:
        tags:
            - trajectories
        summary: Returns all trajectories filter by taxi_id and only date
        description: Returns all trajectories (taxi_id, date)
        parameters:
            -   name: taxi_id
                in: path
                description: ID of taxi to return
                required: true
                schema:
                    type: integer
                    format: int64
            -   name: date
                in: path
                description: Date to return
                required: true
                schema:
                    type: string
                    format: date
        responses:
            '200':
                description: OK - All the trajectories were successfully brought
                content:
                    application/json:
                        schema:
                            type: array
                            items:
                                $ref: '#/components/schemas/Trajectorie'
            '404':
                $ref: '#/components/responses/NotFound'
            '500':
                $ref: '#/components/responses/ServerError' 
    """
    try:
        return Trajectories.get_all_trajectories(taxi_id, date)
    except psycopg2.Error as ex:
        return str(ex)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Returns JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


# Register the path and the entities within it
with app.test_request_context():
    spec.path(view=get_taxis)
    spec.path(view=get_trajectories_for_id)

# Generate .yaml
spec_yaml = spec.to_yaml()

# Save in file .yaml
with open('src/static/spec.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml_file.write(spec_yaml)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

# End-of-file
