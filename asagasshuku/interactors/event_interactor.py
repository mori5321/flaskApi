from asagasshuku.database import db
from datetime import datetime, timedelta
from asagasshuku.models import EventDate

class EventInteractor:

  @classmethod
  def create(cls, event, start_date, finish_date):
    db.session.add(event)
    db.session.commit()
    for n in range((finish_date - start_date).days + 1):
      date = start_date + timedelta(n)
      event_date = EventDate(event_id=event.id, date=date)
      db.session.add(event_date)
      db.session.commit()

    return event



