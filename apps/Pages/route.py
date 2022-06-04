from flask import Blueprint, render_template, session
from apps.Database import crud
import os

blueprint = Blueprint('pages', __name__, url_prefix='')


@blueprint.route('/', methods=['GET'])
def main():
    if 'user' in session:
        key = session.get('user')
        data = crud.get_records(key)
    else:
        session['user'] = os.urandom(20).hex()
        data = []
    return render_template('index.html', values=data)
