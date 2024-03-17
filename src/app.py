""" imports """
from flask import Flask, jsonify
from database.db import connection_db

app = Flask(__name__)

@app.route('/taxis', methods=['GET'])
def get_taxis():
    """ Obtener la lista de todos los taxis """
    try:
        conn = connection_db()
        cur = conn.cursor()
        cur.execute('SELECT * FROM taxistest;')
        taxis = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(taxis)
    except Exception as ex:
        return str(ex)



if __name__ == '__main__':
    app.run(debug=True, port=5000)