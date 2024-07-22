# This file handles database operations

from flask_mysqldb import MySQL
import os

def kasithreads_db(app):
    # Use environment variables for sensitive information
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'password')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'database_name')

    mysql = MySQL(app)
    return mysql
