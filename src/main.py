"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Users
from flask_jwt_simple import JWTManager, jwt_required, create_jwt

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'dfsh3289349yhoelqwru9g'
jwt = JWTManager(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

users = []

@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()

    for x in users:
        for k, v in body.items():
            if x[k] != v:
                return jsonify({'message':'User not found'}), 404

    return jsonify({'token': create_jwt(identity=1)})

@app.route('/users', methods=['POST'])
def register():
    body = request.get_json()

    users.append({
        "email": body['email'],
        "password": body['password'],
        "first_name": body['first_name'],
        "last_name": body['last_name']
    })

    return jsonify({
        'message': 'ok',
        'token': create_jwt(identity=1)
        }), 200

@app.route('/users/<int:id>', methods=['PUT'])
@jwt_required
def edit_user(id):
    
    if id+1 > len(users):
        return jsonify({'message':'User not found'}), 404

    user = users[id]
    body = request.get_json()

    if 'email' in body:
        user['email'] = body['email']
    if 'password' in body:
        user['password'] = body['password']
    if 'first_name' in body:
        user['first_name'] = body['first_name']
    if 'last_name' in body:
        user['last_name'] = body['last_name']

    users[id] = user

    return jsonify(user)


# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
