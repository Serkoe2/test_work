from flask import Blueprint, render_template
blueprint = Blueprint('pages', __name__, url_prefix='')


@blueprint.route('/', methods=['GET'])
def main():
    print(dir(blueprint))
    return render_template('index.html')
