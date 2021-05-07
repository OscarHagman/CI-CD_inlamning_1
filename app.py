from flask import Flask
from handlers.calculator_api import configure_api

app = Flask(__name__)

configure_api(app)

if __name__ == '__main__':
    app.run()
