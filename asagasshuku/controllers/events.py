from flask import Blueprint, make_response, jsonify, request
from IPython import embed
from IPython.terminal.embed import InteractiveShellEmbed
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

from asagasshuku.models import Event, EventSchema, EventDate
from asagasshuku.database import db
from asagasshuku.interactors import EventInteractor

app = Blueprint('events', __name__)


# >>response
# [
#   {
#     "created_at": "2018-12-17T19:03:50.453800+00:00",
#     "id": 1,
#     "title": "Asagasshuku1st",
#     "updated_at": "2018-12-17T19:03:50.453816+00:00"
#   }
# ]
@app.route("/")
def index():
  events = Event.query.all()
  jsonEvents = map(lambda event: EventSchema().dump(event).data, events)
  return make_response(jsonify(list(jsonEvents)))


# @param title: String
# @param start_date: Date
# @param finish_date: Date
# >> response
# {
#   "events_dates": [
#     {
#       "date": "Mon, 01 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 1
#     },
#     {
#       "date": "Tue, 02 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 2
#     },
#     {
#       "date": "Wed, 03 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 3
#     },
#     {
#       "date": "Thu, 04 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 4
#     },
#     {
#       "date": "Fri, 05 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 5
#     }
#   ],
#   "id": 1,
#   "title": "Asagasshuku1st"
# }
@app.route("/", methods=["POST"])
def create():
  event = Event(title=request.form["title"])
  start_date = parse(request.form["start_date"])
  finish_date = parse(request.form["finish_date"])
  event = EventInteractor.create(event, start_date, finish_date)
  return make_response(jsonify(event.to_dict()))


# @param id: Integer
# >> response
# {
#   "events_dates": [
#     {
#       "date": "Mon, 01 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 1
#     },
#     {
#       "date": "Tue, 02 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 2
#     },
#     {
#       "date": "Wed, 03 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 3
#     },
#     {
#       "date": "Thu, 04 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 4
#     },
#     {
#       "date": "Fri, 05 Jan 2018 00:00:00 GMT",
#       "event_id": 1,
#       "id": 5
#     }
#   ],
#   "id": 1,
#   "title": "Asagasshuku1st"
# }
@app.route("/<int:id>")
def show(id):
  event = Event.query.get(id)
  # jsonEvent = EventSchema().dump(event).data
  return make_response(jsonify(event.to_dict()))





@app.route("/<int:id>/result")
def result(id):
  event = Event.query.get(id)
  embed()
  # TODO: calculate result and make a response!
  return make_response(jsonify(event.to_dict()))
