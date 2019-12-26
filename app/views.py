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
    return "Hello, Newcomers"

@bp.route('/query/<int:query_id>')
def query(query_id):
    db = get_db()
    cur = db.cursor()
    if query_id == 1:
        cur.execute(QUERY1)
        headers = HEADERS1
    elif query_id == 2:
        cur.execute(QUERY2)
        headers = HEADERS2
    elif query_id == 3:
        cur.execute(QUERY3)
        headers = HEADERS3
    elif query_id == 4:
        cur.execute(QUERY4)
        headers = HEADERS4

    result = transform_to_json(headers, cur.fetchall())
    return jsonify(result)