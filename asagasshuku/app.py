from flask import Flask, jsonify, make_response, request
from IPython import embed
from IPython.terminal.embed import InteractiveShellEmbed

from asagasshuku.database import db, init_db
from asagasshuku.models import Todo, TodoSchema

from asagasshuku.controllers import events

def create_app():
  app = Flask(__name__)
  app.config.from_object('asagasshuku.config.Config')
  init_db(app)

  app.register_blueprint(events.app, url_prefix="/events")

  # @app.route('/todos')
  # def index():
  #   todos = Todo.query.all()
  #   jsonTodos = map(lambda todo: TodoSchema().dump(todo).data, todos)
  #   return make_response(jsonify(list(jsonTodos)))

  # @app.route('/todos', methods=["POST"])
  # def create():
  #   todo = Todo(name=request.form["name"])
  #   db.session.add(todo)
  #   db.session.commit()
  #   jsonTodo = TodoSchema().dump(todo).data
  #   return make_response(jsonify(jsonTodo))

  return app

app = create_app()

