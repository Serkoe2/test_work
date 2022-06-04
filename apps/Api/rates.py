from flask import Blueprint, jsonify, request, session
from datetime import datetime, date
from apps.Database import crud
import requests

blueprint = Blueprint('rates', __name__, url_prefix='/api/getRates')

# Cache
LAST_UPDATE = None
RatePares = {
    "usd": 0,
    "gbp": 0,
    "eur": 0
}

def getRatePares(key):
    global LAST_UPDATE
    global RatePares
    if LAST_UPDATE is None or LAST_UPDATE < date.today():
        Load = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
        RatePares = {
            "usd": Load["Valute"]["USD"]["Value"],
            "eur": Load["Valute"]["EUR"]["Value"],
            "gbp": Load["Valute"]["GBP"]["Value"]
            }
        LAST_UPDATE = date.today()
    if key in RatePares:
        return RatePares[key]

@blueprint.route('/', methods=['POST'])
def getRates():
    if 'user' in session:
        key = session.get('user')
    else:
        session['user'] = os.urandom(20).hex()
    query = request.get_json()
    if 'rate' not in query or\
       'value' not in query :
       return jsonify({"status": False})
    k = getRatePares(query['rate'])
    result = round(query['value'] * k, 2)
    crud.add_record(key, str(result))
    return jsonify({"status": True, "result": result})
