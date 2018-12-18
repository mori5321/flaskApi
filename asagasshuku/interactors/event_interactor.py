from asagasshuku.database import db
from datetime import datetime, timedelta
from asagasshuku.models import EventDate

class EventInteractor:

  @classmethod
  def create(cls, event, start_date, finish_date):
    db.session.add(event)
    db.session.commit()
    cls.__create_event_dates_from_start_date_and_finish_date(event, start_date, finish_date)

    return event

  @classmethod
  def __create_event_dates_from_start_date_and_finish_date(cls, event, start_date, finish_date):
    for n in range((finish_date - start_date).days + 1):
      date = start_date + timedelta(n)
      event_date = EventDate(event_id=event.id, date=date)
      db.session.add(event_date)
      db.session.commit()



