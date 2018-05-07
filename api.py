"""
RESTful service to run a Goodtables Table Schema validator against a POSTed data file.

Using no validator (applies the GoodTables default validator only)

    curl -F 'file=@files/budget.csv'   http://localhost:5000/

Using validator defined in a local file

    curl -F 'schema=@files/table_schema.json' -F 'file=@files/budget.csv'   http://localhost:5000/

Using validator defined at a URL

    curl -F 'file=@files/budget.csv' -F 'schema_url=https://raw.githubusercontent.com/18F/goodtables-py/master/table_schema.json' http://localhost:5000/

"""

import io
import json
import os

import goodtables
import requests
import werkzeug
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument(
    'file',
    type=werkzeug.FileStorage,
    location='files',
    required=True,
    help='Data file to validate.  Needs valid file extension.')
parser.add_argument(
    'schema',
    type=werkzeug.FileStorage,
    location='files',
    help='Table Schema JSON file to validate data against.')
parser.add_argument(
    'schema_url',
    type=str,
    help='URL of Table Schema JSON file to validate data against.')


def get_schema(post_args):
    """Returns schema in Python format, if provided as uploaded file or URL"""

    if post_args['schema']:
        schema_file = post_args['schema'].stream
        return json.load(schema_file)
    elif post_args['schema_url']:
        resp = requests.get(post_args['schema_url'])
        return resp.json()


class Validate(Resource):
    def get(self):

        return {'things': 'stuff'}

    def post(self):

        post_args = parser.parse_args()
        schema = get_schema(post_args)
        contents = post_args['file'].stream.read()
        format = post_args['file'].filename.split('.')[-1]
        return goodtables.validate(
            io.BytesIO(contents), format=format, schema=schema)


api.add_resource(Validate, '/')

if __name__ == '__main__':
    debug = os.getenv("DEBUG", default=False)
    port = int(os.getenv("VCAP_APP_PORT", default=5000))
    app.run(debug=debug, port=port, host='0.0.0.0')
