""" Imports """
import psycopg2
from database.db import connection_db

class Taxis():
    """Class representing a taxis"""

    @classmethod
    def get_taxis(cls):
        """ Method to get all taxis"""
        try:
            conn = connection_db()
            cur = conn.cursor()
            cur.execute('SELECT * FROM taxis;')
            taxis = cur.fetchall()
            cur.close()
            conn.close()
            return [{'id': taxi[0], 'plate': taxi[1]} for taxi in taxis]
        except psycopg2.Error as ex:
            return str(ex)
