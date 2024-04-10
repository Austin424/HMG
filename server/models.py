from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
import string, datetime



metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)
db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__= "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    profile_pic = db.Column(db.String)
    

class Platform(db.Model, SerializerMixin):
    __tablename__= "platform"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
class Game(db.Model, SerializerMixin):
    __tablename__= "game"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    box_art = db.Column(db.String, nullable=False)
    developer = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    
class GamePlatform(db.Model, SerializerMixin):
    __tablename__= "game_platform"
    id = db.Column(db.String, primary_key=True)
    game_id = db.Column(db.String, db.ForeignKey("game.id"))
    platform_id = db.Column(db.String, db.ForeignKey("platform.id"))
    serialize_rules = ["-game.gameplatform"]
    
class GameProfile(db.Model, SerializerMixin):
    __tablename__= "game_profile"
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.String, db.ForeignKey("game.id"))
    user_id = db.Column(db.String, db.ForeignKey("user.id"))