from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Test(Resource):
    def get(self):
        return {'message': 'yyay'}


api.add_resource(Test, '/test')


app.run(debug=True)
