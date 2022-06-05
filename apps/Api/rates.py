from flask import Blueprint, jsonify, request, session
from datetime import datetime, date
import requests
import os

from apps.Database import crud
from apps import redis_client

blueprint = Blueprint('rates', __name__, url_prefix='/api')


def getRatePares(key):
    LAST_UPDATE = redis_client.get('LAST_UPDATE')
    d = date.today()
    today = datetime(d.year, d.month, d.day) 
    print(LAST_UPDATE)
    if LAST_UPDATE is None or \
        datetime.strptime(LAST_UPDATE, "%Y.%m.%d") < today:
        Load = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
        LAST_UPDATE = today
        redis_client.set("usd", Load["Valute"]["USD"]["Value"])
        redis_client.set("eur", Load["Valute"]["EUR"]["Value"])
        redis_client.set("LAST_UPDATE", date.today().strftime("%Y.%m.%d"))
        redis_client.set("gbp", Load["Valute"]["GBP"]["Value"])
        return Load["Valute"][key.upper()]["Value"]
    return float(redis_client.get(key))


@blueprint.route('/getRates/', methods=['POST'])
def getRates():
    if 'user' in session:
        key = session.get('user')
    else:
        session['user'] = os.urandom(20).hex()
    query = request.get_json()
    if 'rate' not in query or\
       'value' not in query :
       return jsonify({"status": False, "result": "missing params"})
    # проверка Rate и Value
    check_rate = query['rate'] in ['usd', 'eur', 'gbp']
    check_value = isinstance(query['value'], float) or isinstance(query['value'], int) 
    if not check_rate or not check_value:
        return jsonify({"status": False, "result": "incorrect value"})
    k = getRatePares(query['rate'])
    result = round(query['value'] * k, 2)
    crud.add_record(key, str(result))
    return jsonify({"status": True, "result": result})

@blueprint.route('/clearStory/', methods=['POST'])
def clearStory():
    if 'user' not in session:
        return jsonify({"status": False, "result": "user not found"})
    key = session.get('user')
    crud.clear_story(key)
    return jsonify({"status": True, "result": "OK"})