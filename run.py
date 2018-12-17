from asagasshuku.app import app

if __name__ == '__main__':
  app.run(debug=True)

# from flask import Flask, jsonify
# import psycopg2
# from psycopg2.extras import DictCursor
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate



# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/flask_api"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# # migrate Migrate(app, db)

# conn = psycopg2.connect("dbname=flask_api")
# cur = conn.cursor(cursor_factory=DictCursor)

# tasks = {
#   "id": 1
# }

# @app.route('/')
# def index():
#   return jsonify({"tasks": tasks})

# if __name__ == "__main__":
#   app.run(debug=True)





