from flask import Blueprint
from flask import jsonify

from app import cross_origin

from app.db import get_db
from config import HEADERS1, HEADERS2, HEADERS3, HEADERS4
from config import QUERY1, QUERY2, QUERY3, QUERY4
from app.helpers import transform_to_json

bp = Blueprint("routes", __name__)

@bp.route('/')
@cross_origin()
def hello():
    db = get_db()
    cur = db.cursor()
    cur.execute(QUERY1)
    persons = []
    for header, item in cur.fetchall():
        persons.append(item)
    print(persons)
    return 'good'

@bp.route('/query1', methods=['GET'])
@cross_origin()
def query1():
    db = get_db()
    cur = db.cursor()
    cur.execute(QUERY1)
    result = transform_to_json(HEADERS1, cur.fetchall())
    return jsonify(result)

@bp.route('/query2', methods=['GET'])
@cross_origin()
def query2():
    db = get_db()
    cur = db.cursor()
    cur.execute(QUERY2)
    result = transform_to_json(HEADERS2, cur.fetchall())
    return jsonify(result)

@bp.route('/query3', methods=['GET'])
@cross_origin()
def query3():
    db = get_db()
    cur = db.cursor()
    cur.execute(QUERY3)
    result = transform_to_json(HEADERS3, cur.fetchall())
    return jsonify(result)

@bp.route('/query4', methods=['GET'])
@cross_origin()
def query4():
    db = get_db()
    cur = db.cursor()
    cur.execute(QUERY4)
    result = transform_to_json(HEADERS4, cur.fetchall())
    return jsonify(result)