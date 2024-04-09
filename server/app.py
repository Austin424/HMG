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



if __name__ == "__main__":
    app.run(port=5555, debug=True)