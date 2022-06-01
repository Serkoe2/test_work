from flask import Blueprint, jsonify

blueprint = Blueprint('rates', __name__, url_prefix='/api/getRates')


@blueprint.route('/', methods=['GET', 'POST'])
def getRates():
    return jsonify({"status": "OK"})
