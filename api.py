from flask import Flask
from flask_restful import Resource, Api, reqparse, request
import werkzeug
import io
import goodtables

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
# parser.add_argument('file')
parser.add_argument('file', type=werkzeug.FileStorage,
    location='files')

# , type=int, help='Rate to charge for this resource')

class Validate(Resource):

    def post(self):

        file = request.files['file']
        contents = file.stream.read()
        format = file.filename.split('.')[-1]
        import pdb; pdb.set_trace()
        result = goodtables.validate(io.BytesIO(contents), format=format)

        return result

api.add_resource(Validate, '/')

if __name__ == '__main__':
    app.run(debug=True)