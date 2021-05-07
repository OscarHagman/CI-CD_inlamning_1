from flask import request
import json
from flask_restful import Api, Resource


def configure_api(app):

    class Add(Resource):
        def post(self):
            posted_data_string = request.get_data()
            posted_data_json = json.loads(posted_data_string)

            x = posted_data_json.get("x")
            y = posted_data_json.get("y")
            result = x + y

            return_dict = {
                "Result": result,
                "Status Code": 200
            }
            json_result = json.dumps(return_dict)
            return json_result

    api = Api(app)
    api.add_resource(Add, "/add")
