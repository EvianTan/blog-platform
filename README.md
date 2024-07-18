# Blog Platform
A simple blog platform built with Flask, SQLAlchemy, and SQLite. The platform supports user authentication and allows users to create, read, update, and delete blog posts.


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [References](#References)
- [License](#License)


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
4. **Configure the application**:
    Create a `config.py` file in the root directorywith the following content:
    ```python
    import os

    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///instance/blogging_platform.db'
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    ```
    Or you can use `config-example.py` as an example
5. **Set up the database**:
    ```sh
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```
6. **Seed the database with initial testing data** (optional):
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
### User Authentication
- **Sign up a new user**: `POST /auth/signup`
    ```json
    {
        "username": "yourusername",
        "password": "yourpassword"
    }
    ```
- **Sign in an existing user**: `POST /auth/signin`
    - Use Basic Auth with your username and password.
### Blog Posts
- **Create a new post**: `POST /posts`
    ```json
    {
        "title": "Post Title",
        "body": "Post Body"
    }
    ```
    - Protected route, requires authentication.
- **Retrieve All Posts**: `GET /posts`
- **Retrieve a specific post by ID**: `GET /posts/<id>`
    - Protected route, requires authentication.
- **Update an existing post by ID**: `PUT /posts/<id>`
    ```json
    {
        "title": "Updated Title",
        "body": "Updated Body"
    }
    ```
    - Protected route, requires authentication.
- **Delete a post by ID**: `DELETE /posts/<id>`
    - Protected route, requires authentication.


## Testing
1. **Set up the test environment**:
    - Ensure your virtual environment is activated.
    - Install the required dependencies if you haven't already:
      ```sh
      pip install -r requirements.txt
      ```
2. **Run tests**:
    ```sh
    python -m unittest discover tests
    ```



## Troubleshooting
### Common Issues
1. Database Errors:
  - Ensure SQLALCHEMY_DATABASE_URI points to the correct database file.
  - Run `flask db migrate` to test schema changes
  - If you encounter missing tables, run `flask db upgrade` to apply migrations.
2. Authentication Issues:
  - Use Basic Auth for protected routes.
  - Clear browser cache to test authentication changes.
3. Environment Setup:
  - Ensure your virtual environment is activated before running commands.
  - Install all dependencies listed in requirements.txt.


## References
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Migrate Documentation](https://flask-migrate.readthedocs.io/)
- [Flask-HTTPAuth Documentation](https://flask-httpauth.readthedocs.io/)
- [Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)


## License
This project is licensed under the MIT License. 
### MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
2. The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

For more details, see the [LICENSE](LICENSE) file.
