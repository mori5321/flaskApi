from datetime import datetime
from asagasshuku.database import db
from flask_marshmallow import Marshmallow

class Event(db.Model):
  __tablename__ = "events"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "events_dates": [date.to_dict() for date in self.event_dates]
    }

ma = Marshmallow()
class EventSchema(ma.ModelSchema):
  class Meta:
    model = Event

