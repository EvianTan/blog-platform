from base64 import b64encode
import unittest

from flask import json
from app import create_app, db
from app.models import User, Post
from werkzeug.security import generate_password_hash

class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.client = self.app.test_client()

        self.user = User(username='test', password_hash=generate_password_hash('password'))
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_signup(self):
        response = self.client.post('/auth/signup', json={'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 201)

    def test_signin(self):
        # Test signing in with the created user
        credentials = ('test', 'password')
        response = self.client.post('/auth/signin', headers={
            'Authorization': 'Basic ' + b64encode(f"{credentials[0]}:{credentials[1]}".encode('utf-8')).decode('utf-8')
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Logged in successfully', json.loads(response.data)['message'])
        
    def test_create_post(self):
        # Encode credentials for Basic Auth
        credentials = ('test', 'password')
        auth_header = {
            'Authorization': 'Basic ' + b64encode(f"{credentials[0]}:{credentials[1]}".encode('utf-8')).decode('utf-8')
        }

        # Sign in the user first
        response = self.client.post('/auth/signin', headers=auth_header)
        self.assertEqual(response.status_code, 200)

        # Create a new post
        response = self.client.post('/posts', json={'title': 'New Post', 'body': 'Post Body'}, headers=auth_header)
        self.assertEqual(response.status_code, 201)

    def test_get_posts(self):
        # Create some dummy posts
        post1 = Post(title='Post 1', body='Body 1')
        post2 = Post(title='Post 2', body='Body 2')
        db.session.add_all([post1, post2])
        db.session.commit()

        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200)
        posts = json.loads(response.data)
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]['title'], 'Post 1')
        self.assertEqual(posts[1]['title'], 'Post 2')
    
    def test_get_post(self):
        post = Post(title='Test Post', body='Test Body')
        db.session.add(post)
        db.session.commit()

        credentials = ('test', 'password')
        auth_header = {
            'Authorization': 'Basic ' + b64encode(f"{credentials[0]}:{credentials[1]}".encode('utf-8')).decode('utf-8')
        }

        # Retrieve the post by its ID using session.query
        post_id = post.id
        response = self.client.get(f'/posts/{post_id}', headers=auth_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['title'], 'Test Post')

    def test_update_post(self):
        post = Post(title='Test Post', body='Test Body')
        db.session.add(post)
        db.session.commit()

        credentials = ('test', 'password')
        auth_header = {
            'Authorization': 'Basic ' + b64encode(f"{credentials[0]}:{credentials[1]}".encode('utf-8')).decode('utf-8')
        }

        # Update the post
        updated_data = {'title': 'Updated Post', 'body': 'Updated Body'}
        response = self.client.put(f'/posts/{post.id}', json=updated_data, headers=auth_header)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Post updated', json.loads(response.data)['message'])

    def test_delete_post(self):
        post = Post(title='Test Post', body='Test Body')
        db.session.add(post)
        db.session.commit()

        # Delete the post
        response = self.client.delete(f'/posts/{post.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Post deleted', json.loads(response.data)['message'])

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
