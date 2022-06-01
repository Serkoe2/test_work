from flask import Blueprint

blueprint = Blueprint('rates', __name__, url_prefix='/api/getRates')


@blueprint.route('/', methods=['GET', 'POST'])
def getRates():
    return "OK"
