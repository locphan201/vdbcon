from flask import Blueprint, render_template

page_blueprint = Blueprint('pages', __name__)

@page_blueprint.route('/', methods=['GET'])
def connector():
    return render_template('connector.html')