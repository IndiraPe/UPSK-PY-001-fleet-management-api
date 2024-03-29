""" Imports """
import psycopg2
from flask import jsonify
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
            return jsonify([{'id': taxi[0], 'plate': taxi[1]} for taxi in taxis])
        except psycopg2.Error as ex:
            return str(ex)

class Trajectories():
    """ Class representing a trajectories """

    @classmethod
    def get_all_trajectories(cls, taxi_id, date):
        """ Method to get all trajectories with id and date """
        cls.id = taxi_id
        cls.date = date
        try:
            conn = connection_db()
            cur = conn.cursor()
            cur.execute("SELECT * FROM trajectories \nWHERE taxi_id = %s \nAND DATE(date) = %s;", (taxi_id, date))  # pylint: disable=line-too-long
            trajectories = cur.fetchall()
            cur.close()
            conn.close()
            return jsonify([{'taxi_id': trajectorie[1], 'date': trajectorie[2], 'latitude': trajectorie[3], 'longitude': trajectorie[4]} for trajectorie in trajectories])  # pylint: disable=line-too-long
        except psycopg2.Error as ex:
            return str(ex)
