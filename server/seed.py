from app import app
from models import db, Game

# from flask import Flask

# {
#     "id": 1,
#     "title": "Overwatch 2",
#     "boxArt": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.mobygames.com%2Fcovers%2F11037275-overwatch-2-xbox-one-front-cover.png&f=1&nofb=1&ipt=ea5124965d60b1be2344b2afe222776af97dea12e06a573c1e4b843ae276721d&ipo=images",
#     "developer": "Blizzard Entertainment",
#     "publisher": "Blizzard Entertainment",
#     "genre": ["First-person shooter", "Hero Shooter"]
# }

print(">> Seeding... starting...")

with app.app_context():
    print(">> Deleting previous data...")
    Game.query.delete()
    
    print(">> Creating unique games as object relational entries...")
    ow_game_1 = Game(name="Overwatch 2", 
         box_art="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.mobygames.com%2Fcovers%2F11037275-overwatch-2-xbox-one-front-cover.png&f=1&nofb=1&ipt=ea5124965d60b1be2344b2afe222776af97dea12e06a573c1e4b843ae276721d&ipo=images", 
         developer="Blizzard Entertainment", 
         publisher="Blizzard Entertainment", 
         genre="Hero Shooter")
    # sm_game_2 = ???
    # ??_game_3 = ???
    seeded_games = [ow_game_1] # eventually... [ow_game_1, sm_game_2, ??_game_3, ...]
    
    print(">> Adding games to database...")
    db.session.add_all(seeded_games)
    db.session.commit()

    print(">> Seeding... done.")