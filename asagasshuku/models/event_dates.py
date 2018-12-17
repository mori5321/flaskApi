from datetime import datetime
from asagasshuku.database import db
from flask_marshmallow import Marshmallow

class EventDate(db.Model):
  __tablename__ = "event_dates"

  id = db.Column(db.Integer, primary_key=True)
  event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
  event = db.relationship('Event', backref="event_dates")
  date = db.Column(db.DateTime, nullable=False, default=datetime.now)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def to_dict(self):
    return {
      "id": self.id,
      "date": self.date,
      "event_id": self.event_id
    }


ma = Marshmallow()
class EventDateSchema(ma.ModelSchema):
  class Meta:
    model = EventDate
