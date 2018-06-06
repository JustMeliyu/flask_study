# encoding:utf-8

from flask import Blueprint, request, json, render_template

t_json = Blueprint('t_json', __name__)


@t_json.route('/t_json', methods=['GET', 'POST'])
def test_json():
    if request.method == 'GET':
        print request.values[0]
        print request.json
        print request.get_json(force=False, silent=True)
    return render_template('test_html.html')
