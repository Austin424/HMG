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
    serialize_rules = ['-game_profiles.user']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    handle = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    location = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    profile_pic = db.Column(db.String)
    

    
    

class Platform(db.Model, SerializerMixin):
    __tablename__= "platform"
    serialize_rules = ['-game_platforms.platform']
    id = db.Column(db.Integer, primary_key=True)
    console = db.Column(db.String, nullable=False)
    logo = db.Column(db.String)
    
    game_platforms = db.relationship("GamePlatform", back_populates="platform")
    
class Game(db.Model, SerializerMixin):
    __tablename__= "game"
    serialize_rules = ['-game_platforms.game']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    boxart = db.Column(db.String, nullable=False)
    developer = db.Column(db.String, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    
    game_platforms = db.relationship('GamePlatform', back_populates="game")
    
class Team(db.Model, SerializerMixin):
    __tablename__ = "team_finder"
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    role = db.Column(db.String)
    open_spots = db.Column(db.Integer)
    

    
class GamePlatform(db.Model, SerializerMixin):
    __tablename__= "game_platform"
    serialize_rules = ['-game.game_platforms',   '-platform.game_platforms'] 
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    platform_id = db.Column(db.Integer, db.ForeignKey("platform.id"))

    
    game = db.relationship("Game", back_populates="game_platforms")
    platform = db.relationship("Platform", back_populates="game_platforms")
    
class GameProfile(db.Model, SerializerMixin):
    __tablename__= "game_profile"
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

