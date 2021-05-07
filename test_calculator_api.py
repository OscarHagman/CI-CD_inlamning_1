from flask import Flask
import json
from handlers.calculator_api import configure_api


def test_Add():
    app = Flask(__name__)
    configure_api(app)
    client = app.test_client()
    url = "/add"

    mock_request_data = {
        "x": 15,
        "y": 10
    }
    request_json = json.dumps(mock_request_data)

    response = client.post(url, data=request_json)
    assert response.Result == 25
