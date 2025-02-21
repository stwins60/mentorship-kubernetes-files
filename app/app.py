from flask import Flask, jsonify
import os
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# Read configuration from environment variables (set via ConfigMap & Secret)
APP_NAME = os.getenv('APP_NAME', 'Flask Advanced App')
APP_ENV = os.getenv('APP_ENV', 'development')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'flaskdb')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_PORT = os.getenv('DB_PORT', '5432')

# Connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

@app.route('/')
def index():
    return jsonify({
        "app_name": APP_NAME,
        "environment": APP_ENV,
    })

@app.route('/users')
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()

    users_list = [{"id": user[0], "name": user[1]} for user in users]
    
    return jsonify({"source": "database", "users": users_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
