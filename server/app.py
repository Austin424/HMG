# These are the imports which will setup the functions used in this app.py file.
from flask import Flask, make_response, jsonify, request, session, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Platform, GamePlatform, Game, GameProfile
import json

# from flask_cors import CORS
# from flask_bcrypt import Bcrypt


# Here, we're initializing the Database for our use purposes.
app = Flask(__name__)
# We're also running our app in debug mode.
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
# We're also disabling the modification tracking system to conserve on significant computing power.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
migrate = Migrate(app, db)
db.init_app(app)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the HiveMind"}), 200

@app.get("/api/games")
def get_games():
    # Following this route will lead us directly to all of the books in our table.
    games = Game.query.all()
    print(games)
    # So far we're only summonign the books as  Python objects. We still need to convert our book objects into dictionaries.
    game_dicts = []
    for g in games:
        game_dicts.append(g.to_dict())
    return game_dicts, 200

@app.get("/api/games/<int:game_id>")
def get_game_by_id(game_id):
    matching_game = Game.query.filter(Game.id == game_id).first()
    # print(matching_game)
    if not matching_game:
        return make_response(jsonify({"error": f"Game ID `{game_id}` not found in database."}), 404)
    return matching_game.to_dict(), 200






if __name__ == "__main__":
    app.run(port=5555, debug=True)