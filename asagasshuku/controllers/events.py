from flask import Blueprint, make_response, jsonify, request
from IPython import embed
from IPython.terminal.embed import InteractiveShellEmbed
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

from asagasshuku.models import Event, EventSchema, EventDate
from asagasshuku.database import db
from asagasshuku.interactors import EventInteractor

app = Blueprint('events', __name__)

@app.route("/")
def index():
  events = Event.query.all()
  jsonEvents = map(lambda event: EventSchema().dump(event).data, events)
  return make_response(jsonify(list(jsonEvents)))


@app.route("/", methods=["POST"])
def create():
  event = Event(title=request.form["title"])
  start_date = parse(request.form["start_date"])
  finish_date = parse(request.form["finish_date"])
  event = EventInteractor.create(event, start_date, finish_date)
  return make_response(jsonify(event.to_dict()))

@app.route("/<int:id>")
def show(id):
  event = Event.query.get(id)
  # jsonEvent = EventSchema().dump(event).data
  return make_response(jsonify(event.to_dict()))

