import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify
from api.exceptions.custom_exception import CustomException
from api.utils.status_code import HttpStatus
from infrastructure.database import db, migrate
from api.routes.task_routes import todo
from api.routes.authentication_routes import auth
from flask_cors import CORS, cross_origin

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db.init_app(app)
migrate.init_app(app, db)


app.register_blueprint(todo)
app.register_blueprint(auth)

CORS(app, allow_headers=['Content-Type', 'Authorization'])

print(app.url_map)

@app.errorhandler(CustomException)
def handle_exceptions(error):
    return jsonify(error.to_dict()), error.status_code

if __name__ == '__main__':
    app.run()