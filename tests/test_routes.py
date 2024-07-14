import unittest
from app import create_app, db
# from app.models import User, Post
from werkzeug.security import generate_password_hash

class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.client = self.app.test_client()

        # self.user = User(username='test', password_hash=generate_password_hash('password'))
        # db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # def test_signup(self):
    #     response = self.client.post('/signup', json={'username': 'newuser', 'password': 'newpassword'})
    #     self.assertEqual(response.status_code, 201)

    # def test_create_post(self):
    #     response = self.client.post('/signin', auth=('test', 'password'))
    #     self.assertEqual(response.status_code, 200)
        
    #     response = self.client.post('/posts', json={'title': 'New Post', 'body': 'Post Body'}, auth=('test', 'password'))
    #     self.assertEqual(response.status_code, 201)

    # def test_get_posts(self):
    #     response = self.client.get('/posts')
    #     self.assertEqual(response.status_code, 200)

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
