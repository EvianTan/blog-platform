# Documentation:
## Design decisions
1. Use Flask
  - Minimalist Framework
  - Easy to Deploy
2. Use SQLite for database, HTTPAuth for authentication
  - Lightweight
  - Easy to work with Flask
3. Create a simple Flask application
  - A "Hello world" is always needed for testing development environment
  - Also setup a test suite
4. Design APIs for posts
  - Basic CRUD APIs
  - create_post(), get_posts(), get_post(id), update_post(id), delete_post(id)
5. Create model for posts
  - title: string, body: text, id:  auto-incremented integer
6. Create routes for posts with model and API design
  - also create tests for those APIs
7. Test Post's APIs with Postman
  - setup requests
  - create posts, then get/getAll/update/delete
8. Design and create APIs for Users
  - add User model
  - create routes for signup() and signin()
  - also create tests for those APIs
9. Test User's APIs with Postman
10. Update Post's APIs with autentication
  - also update tests for those APIs
11. Test the updated Post's APIs in Postman
  - add Username and Password as Basic Auth in requests' headers

## Trade-offs:
1. While Flask provides simplicity and flexibility, larger applications may require more features and structure provided by full-stack frameworks like Django.
2. Similar trade-off for choosing SQLite, if need more scale database we will use PostgreSQL or MySQL
3. Similar trade-off for choosing Flask-HTTPAuth
4. Use `config.py` to store environments variables is not safe as deploying with CI/CD tools like Docker

## Improvements with More Time:
1. Implement OAuth for third-party authentication and token-based authentication for improved security and usability.
2. Implement robust validation for input data, prevent web security problems (like SQL injection, xss, etc.), better error handling, and informative error responses for API consumers.
3. Expand test coverage to include edge cases, integration tests, and performance tests to ensure application reliability.
4. Setup automation deployment
5. Add signout api
6. Add timestamp for create/delete/update posts and signup/signin/signout users