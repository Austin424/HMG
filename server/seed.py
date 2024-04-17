from app import app
from models import db, Game, User, Platform, GamePlatform, GameProfile
from faker import Faker
import json
import random
fake = Faker()

if __name__ == "__main__":
     
     print(">> Seeding... starting...")

     with app.app_context():
          
          Game.query.delete()
          User.query.delete()
          Platform.query.delete()
          
          games = []
          
          with open("games.json") as f:
               games = json.load(f)
          for game in games["games"]:
               new_game = Game(
                    name=game["name"],
                    boxart=game["boxart"],
                    developer=game["developer"],
                    publisher=game["publisher"],
                    genre=game["genre"]
               )
               db.session.add(new_game)
               db.session.commit()
               
          
          
          

          for i in range(10):
               user = User(name=fake.name(), email=fake.email(),handle=fake.sentence().split(' ')[0], profile_pic=fake.image_url(), location=fake.address(), password=fake.password())
               db.session.add(user)
          db.session.commit()          
          platforms = []
          
          with open("platform.json") as f:
               platforms = json.load(f)
          for platform in platforms["platform"]:
               new_platform = Platform(
                    console=platform["console"],
                    logo=platform["logo"]
               )
               db.session.add(new_platform)
               db.session.commit()
          
          
          
          game_platform = []
          
          for _ in range(21):
               game_platform = GamePlatform(
                    game_id = random.randint(1, len(games["games"])),
                    platform_id = random.randint(1, len(platforms["platform"]))
               )
               db.session.add(game_platform)
          db.session.commit()
          
          game_profile = []
          
          for _ in range(10):
               game_profile = GameProfile(
                    game_id = random.randint(1, len(games["games"])),
                    user_id = random.randint(1,10)
               )
               db.session.add(game_profile)
          db.session.commit()
          
          
          
               
               


          print(">> Seeding... done.")



# print(">> Seeding... starting...")

# with app.app_context():
#     print(">> Deleting previous data...")
#     Game.query.delete()
    
#     print(">> Creating unique games as object relational entries...")
#     ow_game_1 = Game(name="Overwatch 2", 
#          box_art="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.mobygames.com%2Fcovers%2F11037275-overwatch-2-xbox-one-front-cover.png&f=1&nofb=1&ipt=ea5124965d60b1be2344b2afe222776af97dea12e06a573c1e4b843ae276721d&ipo=images", 
#          developer="Blizzard Entertainment", 
#          publisher="Blizzard Entertainment", 
#          genre="Hero Shooter")
#     sm_game_2 = Game(name="Smite", 
#          box_art="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.mobygames.com%2Fcovers%2F3671623-smite-battleground-of-the-gods-gold-bundle-xbox-one-front-cover.png&f=1&nofb=1&ipt=9e307e13963f9c538b6334f6ce654ce32cdc9598abfb06dd2a4102b9adbe9942&ipo=images", 
#          developer="Respawn Entertainment", 
#          publisher="Electronic Arts", 
#          genre="MOBA")
    
    
    
    # sm_game_2 = ???
    # ??_game_3 = ???
#     seeded_games = [ow_game_1] # eventually... [ow_game_1, sm_game_2, ??_game_3, ...]
    
#     print(">> Adding games to database...")
#     db.session.add_all(seeded_games)
#     db.session.commit()

#     print(">> Seeding... done.")
    
          # seed_database()