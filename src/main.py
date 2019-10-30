"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap, sha256
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

@app.route('/')
def home():
    return "<div style='text-align: center; margin-top:10%'><h1>Backend running...</h1><br/><h3>Welcome back samir</h3></div>"

@app.route('/users', methods=['GET'])
def handle_users():

    if request.method == 'GET':
        users = Users.query.all()

        if not users:
            return jsonify({'msg':'User not found'}), 404

        return jsonify( [x.serialize() for x in users] ), 200

    return "Invalid Method", 404


@app.route('/testing', methods=['POST'])
def test():
    return jsonify({'token':'hello world'})
    return jsonify(request.get_json())

@app.route('/login', methods=['POST'])
def handle_login():

    body = request.get_json()

    user = Users.query.filter_by(email=body['email'], password=sha256(body['password'])).first()

    if not user:
        return 'User not found', 404

    return jsonify({
              'token': create_jwt(identity=1),
              'email': user.email,
              'firstname': user.firstname,
              'lastname': user.lastname
              })


@app.route('/register', methods=['POST'])
def handle_register():

    body = request.get_json()

    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'firstname' not in body and 'lastname' not in body:
        raise APIException("You need to specify the first name and last name", status_code=400)
    if 'password' not in body and 'email' not in body:
        raise APIException("You need to specify the password and email", status_code=400)
    if 'firstname' not in body:
        raise APIException('You need to specify the first name', status_code=400)
    if 'lastname' not in body:
        raise APIException('You need to specify the last name', status_code=400)
    if 'password' not in body:
        raise APIException('You need to specify the password', status_code=400)
    if 'email' not in body:
        raise APIException('You need to specify the email', status_code=400)



    db.session.add(Users(
        email = body['email'],
        firstname = body['firstname'],
        lastname = body['lastname'],
        password = sha256(body['password'])
    ))
    db.session.commit()

    return 'success'

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
