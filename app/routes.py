from flask import Blueprint, request, jsonify
from app import db
from app.models import Post
from app.auth import auth

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return 'Hello, World!'

@bp.route('/posts', methods=['POST'])
@auth.login_required
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], body=data['body'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post created'}), 201

@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

@bp.route('/posts/<int:id>', methods=['GET'])
@auth.login_required
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_dict())

@bp.route('/posts/<int:id>', methods=['PUT'])
@auth.login_required
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json()
    post.title = data['title']
    post.body = data['body']
    db.session.commit()
    return jsonify({'message': 'Post updated'})

@bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted'})
