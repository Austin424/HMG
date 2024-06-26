# These are the imports which will setup the functions used in this app.py file.
from flask import Flask, make_response, jsonify, request, session, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User, Platform, GamePlatform, Game, GameProfile, Team
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

# GET Request Across All Data.
@app.get("/api/games")
def get_games():
    # Following this route will lead us directly to all of the games in our table.
    games = Game.query.all()
    print(games)
    # So far we're only summonign the games as  Python objects. We still need to convert our games objects into dictionaries.
    game_dicts = []
    for g in games:
        game_dicts.append(g.to_dict())
    return game_dicts, 200

@app.get("/api/team_posts")
def get_team_posts():
    # Query all team posts from the database
    team_posts = Team.query.all()

    # Convert team post objects into dictionaries
    team_posts_dicts = []
    for tp in team_posts:
        team_posts_dicts.append(tp.to_dict())

    # Return the team posts as JSON with status code 200
    return jsonify(team_posts_dicts), 200


# GET Request for Individual Data Point.
@app.get("/api/games/<int:game_id>")
def get_game_by_id(game_id):
    matching_game = Game.query.filter(Game.id == game_id).first()
    # print(matching_game)
    if not matching_game:
        return make_response(jsonify({"error": f"Game ID `{game_id}` not found in database."}), 404)
    return matching_game.to_dict(), 200

# POST Request to Add New Data Point to Database.

@app.route("/api/team_posts", methods=["POST"])
def add_team_post():
    data = request.get_json()
    
    team_post = Team(
    game_id = data.get('game_id'),
    creator_id = data.get('creator_id'),
    role = data.get('role'),
    open_spots = data.get('open_spots')
    )
    db.session.add(team_post)
    db.session.commit()
    return jsonify(team_post.to_dict()), 201

# PATCH Request to Update Record(s) of Individual Data Point in Database.

# DELETE Request to Delete Individual Data Point from Database.




if __name__ == "__main__":
    app.run(port=5555, debug=True)