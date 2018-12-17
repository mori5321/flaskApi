from datetime import datetime
from asagasshuku.database import db
from flask_marshmallow import Marshmallow

class Todo(db.Model):
  __tablename__ = "todos"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


ma = Marshmallow()
class TodoSchema(ma.ModelSchema):
  class Meta:
    model = Todo
