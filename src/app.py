""" imports """
import psycopg2
from flask import Flask, jsonify, json
from werkzeug.exceptions import HTTPException
from models.taxi import Taxis

app = Flask(__name__)

@app.route('/taxis', methods=['GET'])
def get_taxis():
    """ Obtener la lista de todos los taxis.
    ---
    get:
        tags:
            - taxis
        description: returns all taxis (id, plate)
        responses:
            '200':
            description: "OK"
            content:
                application/json:
                schema:
                    $ref: 'http://127.0.0.1:5000/taxis'
    """
    try:
        taxis = Taxis.get_taxis()
        return jsonify(taxis)
    except psycopg2.Error as ex:
        return str(ex)


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Devuelve JSON en lugar de HTML para errores HTTP."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response



if __name__ == '__main__':
    app.run(debug=True, port=5000)

# End-of-file
