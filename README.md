# blog-platform
A blog platform which written with Python Flask RESTful APIs

## Build a RESTful API for a simple blogging platform

### Requirements:
1. Design and implement a RESTful API using either Python Flask or Django.
2. The API should have endpoints for:
  - Creating a new blog post
  - Retrieving a list of all blog posts
  - Retrieving a single blog post by its ID
  - Updating an existing blog post
  - Deleting a blog post
3. Implement basic authentication for the API. Users should be able to sign up, sign in, and authenticate their requests to create, update, or delete blog posts.
4. Use a database of your choice (e.g., MongoDB, PostgreSQL, MySQL) to store blog post data.
5. Write unit tests to ensure the reliability of your code.

### Evaluation Criteria:
1. Code Quality: Assess the cleanliness, readability, and organization of the code. Look for the effective use of coding best practices and design patterns.
2. System Architecture: Evaluate the architecture of the system, considering factors such as scalability, maintainability, and extensibility.
3. RESTful Design: Check if the API endpoints adhere to RESTful principles and conventions.
   Authentication: Verify the implementation of authentication mechanisms and security measures.
4. Database Usage: Evaluate the interaction with the chosen database, including data modeling and query optimization.
5. Testing: Review the completeness and effectiveness of the unit tests.

### Submission Guidelines:
1. Provide the source code of your project, along with any necessary setup instructions.
2. Include documentation explaining your design decisions, trade-offs made, and any additional features or improvements you would have implemented with more time.

### References:
https://www.codementor.io/@olawalealadeusi896/restful-api-with-python-flask-framework-and-postgres-db-part-1-kbrwbygx5
ChatGPT

### Steps/Plan
Keyword: Python, Flask, CRUD, user, authentication, blog

### Dependencies
Python3
pip3
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

#### 1. Dependencies Install
```bash
pip3 install Flask Flask-SQLAlchemy Flask-Migrate Flask-HTTPAuth
```

#### 2. Set up the project structure:
```bash
blogging_platform/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   ├── routes.py
├── migrations/
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
├── config.py
├── run.py
└── requirements.txt
```

```bash
# Create requirements.txt
echo "Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-HTTPAuth" > requirements.txt

# Install dependencies from requirements.txt
pip3 install -r requirements.txt
```

setup the database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

```bash
set FLASK_APP=run.py
```

#### 3. Create a blog
```bash
curl -u username:password -X POST -H "Content-Type: application/json" -d '{"title": "My First Post", "body": "This is the content of my first post."}' http://127.0.0.1:5000/posts

```
or use Postman
- new post request
- url: http://127.0.0.1:5000/posts
- Go to the "Authorization" tab, choose "Basic Auth," and enter your username and password.
- Go to the "Headers" tab, add a new header with the key Content-Type and value application/json
- Go to the "Body" tab, choose "raw," and enter the following JSON:
  ```json
  {
      "title": "My First Post",
      "content": "This is the content of my first post."
  }
  ```

#### Notes:
`config.py`: store configuration
`app/__init__.py`: create the app
`app/models.py`: define models
`app/routes.py`: define routes for frontend
`run.py`: start this script to run the app