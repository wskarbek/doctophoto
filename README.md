# doctophoto
Web application that allows doctor to send radiography images with description to his patients.

More info coming soon...

# Database setup
You need to create db.py file in project's root directory with your database engine, login credentials:
```python
ENGINE = 'django database engine'
NAME = 'database name'
USER = 'username'
PASSWORD = 'password'
HOST = 'localhost'
PORT = '1234'
```
During development of the project, Docker with Postgres database was used.