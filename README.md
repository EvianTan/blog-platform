# Blog Platform
A simple blog platform built with Flask, SQLAlchemy, and SQLite. The platform supports user authentication and allows users to create, read, update, and delete blog posts.


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)


## Features
- User authentication (sign up, sign in)
- Create, read, update, and delete blog posts
- Basic HTTP authentication for protected routes
- SQLite database for data persistence


## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/EvianTan/blog-platform.git
    cd blog-platform
    ```
2. **Set up a virtual environment (Optional but recommended)**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install dependencies**:
    >Note: Ensure Python and `pip` are installed on your system. If not, download and install Python from [python.org](https://www.python.org/downloads/).
    ```sh
    pip install -r requirements.txt
    ```
4. **Set up the database**:
    ```sh
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
5. **Seed the database with initial testing data** (optional):
    >Note: Populating the database with initial users and posts data
    ```sh
    python seed.py
    ```

## Usage
1. **Run the application**:
    ```sh
    flask run
    ```
2. **Access the application**:
    Open your browser and go to `http://127.0.0.1:5000`.
3. **Test API Endpoints with Postman**:
    - Import the Postman collection `(Python Flask Blog Platform.postman_collection.json`) into your Postman application.
    - Modify the requests as needed to suit your testing or integration requirements.
  

## API Endpoints
### Authentication
- **Sign Up**: `POST /auth/signup`
    ```json
    {
        "username": "yourusername",
        "password": "yourpassword"
    }
    ```
- **Sign In**: `POST /auth/signin`
    - Use Basic Auth with your username and password.
### Blog Posts
- **Create Post**: `POST /posts`
    ```json
    {
        "title": "Post Title",
        "body": "Post Body"
    }
    ```
    - Protected route, requires authentication.
- **Get All Posts**: `GET /posts`
- **Get Single Post**: `GET /posts/<id>`
    - Protected route, requires authentication.
- **Update Post**: `PUT /posts/<id>`
    ```json
    {
        "title": "Updated Title",
        "body": "Updated Body"
    }
    ```
    - Protected route, requires authentication.
- **Delete Post**: `DELETE /posts/<id>`
    - Protected route, requires authentication.


## Testing
1. **Run tests**:
    ```sh
    python -m unittest discover tests
    ```
2. **Example test case**:
    ```python
    def test_signup(self):
        response = self.client.post('/auth/signup', json={'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 201)
    ```


## Configuration
Configuration settings are in `config.py`. You can override them using environment variables.
### Default Config
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///instance/blogging_platform.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```


## Troubleshooting
### Common Issues
1. Database Errors:
  - Ensure SQLALCHEMY_DATABASE_URI points to the correct database file.
  - If you encounter missing tables, run flask db upgrade to apply migrations.
2. Authentication Issues:
  - Use Basic Auth for protected routes.
  - Clear browser cache or use incognito mode to test authentication changes.
3. Environment Setup:
  - Ensure your virtual environment is activated before running commands.
  - Install all dependencies listed in requirements.txt.


## License
This project is licensed under the MIT License. 
### MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
2. The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

For more details, see the [LICENSE](LICENSE) file.
