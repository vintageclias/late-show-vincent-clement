from flask import Blueprint, jsonify, request
from .models import db, Episode, Guest, Appearance

api = Blueprint('api', __name__)

@api.route('/episodes')
def get_episodes():
    return jsonify([e.to_dict() for e in Episode.query.all()])

@api.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict())
    return jsonify({"error": "Episode not found"}), 404

@api.route('/guests')
def get_guests():
    return jsonify([g.to_dict() for g in Guest.query.all()])

@api.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get("rating")
    episode_id = data.get("episode_id")
    guest_id = data.get("guest_id")

    if not (1 <= rating <= 5):
        return jsonify({"errors": ["validation errors"]}), 400

    episode = Episode.query.get(episode_id)
    guest = Guest.query.get(guest_id)

    if not episode or not guest:
        return jsonify({"errors": ["Invalid episode or guest"]}), 400

    appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
    db.session.add(appearance)
    db.session.commit()
    return jsonify(appearance.to_dict()), 201
