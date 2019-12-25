import psycopg2

from flask import g
from config import USER, DBNAME, PASSWORD, HOST, PORT


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            database=DBNAME,
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            connect_timeout=20
        )
    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()


def init_app(app):
    app.teardown_appcontext(close_db)
