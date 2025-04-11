
from . import db
from .models import Episode, Guest, Appearance
from flask import Flask
from app import create_app

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

# Example fallback seed data:
guests = [
    Guest(name="Michael J. Fox", occupation="actor"),
    Guest(name="Sandra Bernhard", occupation="Comedian"),
    Guest(name="Tracey Ullman", occupation="television actress"),
]

episodes = [
    Episode(date="1/11/99", number=1),
    Episode(date="1/12/99", number=2),
]

db.session.add_all(guests + episodes)
db.session.commit()

appearances = [
    Appearance(rating=4, guest_id=1, episode_id=1),
    Appearance(rating=5, guest_id=3, episode_id=2),
]

db.session.add_all(appearances)
db.session.commit()
print("Seeded!")
