from flask import Blueprint, jsonify, request, g
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User
from flask_httpauth import HTTPBasicAuth

bp = Blueprint('auth', __name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        g.user = user
        return True
    return False

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'User already exists'}), 400
    user = User(username=username, password_hash=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@bp.route('/signin', methods=['POST'])
@auth.login_required
def signin():
    return jsonify({'message': 'Logged in successfully'}), 200
