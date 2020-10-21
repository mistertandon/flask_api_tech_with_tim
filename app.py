from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    def get(self, name, age):
        return {
            'name': name,
            'age': age
        }


api.add_resource(HelloWorld, "/hello/<string:name>/<int:age>")

if __name__ == "__main__":
    app.run(debug = True)