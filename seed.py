from app import create_app, db
from app.models import User, Post
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Create test users
    users = [
        User(username='user1', password_hash=generate_password_hash('password1')),
        User(username='user2', password_hash=generate_password_hash('password2'))
    ]
    for user in users:
        db.session.add(user)
    db.session.commit()

    # Create test posts
    posts = [
        Post(title='First Post', body='This is the body of the first post'),
        Post(title='Second Post', body='This is the body of the second post')
    ]
    for post in posts:
        db.session.add(post)
    db.session.commit()
