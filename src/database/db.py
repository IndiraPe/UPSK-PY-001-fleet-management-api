""" Importaciones """
import os
import psycopg2
from psycopg2 import DatabaseError
from dotenv import load_dotenv

load_dotenv(".env.development.local")

def connection_db():
    """ Connect to database in Vercel-postgreSQL """
    try:
        return psycopg2.connect(
            host = os.getenv("POSTGRES_HOST"),
            user = os.getenv("POSTGRES_USER"),
            password = os.getenv("POSTGRES_PASSWORD"),
            database = os.getenv("POSTGRES_DATABASE")
        )
    except DatabaseError as ex:
        raise ex

# End-of-file
