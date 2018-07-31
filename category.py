from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Sport, Base, SportItem, User

engine = create_engine('sqlite:///sportcategorieswithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Savneet Singh", email="s_k_singh94@hotmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User1)
session.commit()

# Menu for Football
sport1 = Sport(user_id=User1.id, name="Football")

session.add(sport1)
session.commit()


sportItem1 = SportItem(
 user_id=User1.id, name="Ball",
 description="Leather ball, one per game.", sport=sport1)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(
 user_id=User1.id, name="Gloves",
 description="Goalie uses gloves to protect hands.", sport=sport1)

session.add(sportItem2)
session.commit()

sportItem3 = SportItem(
 user_id=User1.id, name="Net",
 description="Two nets in each pitch, opposite ends.", sport=sport1)

session.add(sportItem3)
session.commit()

sportItem4 = SportItem(
 user_id=User1.id, name="Soccer Cleats",
 description="Used for protection", sport=sport1)

session.add(sportItem4)
session.commit()

sportItem5 = SportItem(
 user_id=User1.id, name="Jersey",
 description="Each team has their own Jersey with their team logo on.",
 sport=sport1)

session.add(sportItem5)
session.commit()


sportItem6 = SportItem(
 user_id=User1.id, name="Boots",
 description="Leather boots with studs needed to play and get better grip",
 sport=sport1)

session.add(sportItem6)
session.commit()


# Menu for Basketball
sport2 = Sport(user_id=User1.id, name="Basketball")

session.add(sport2)
session.commit()

sportItem1 = SportItem(
 user_id=User1.id, name="Basketball",
 description="One per game. Can be dribbled and shot through the hoops.",
 sport=sport2)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(
 user_id=User1.id, name="Hoops",
 description="2, 1 on either side of court", sport=sport2)

session.add(sportItem2)
session.commit()


# Menu for Horse Riding
sport3 = Sport(user_id=User1.id, name="Horse Riding")

session.add(sport3)
session.commit()


sportItem1 = SportItem(
 user_id=User1.id, name="Horse",
 description="To be ridden.", sport=sport3)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(
 user_id=User1.id, name="Rein",
 description="Used to steer horse", sport=sport3)

session.add(sportItem2)
session.commit()

sportItem3 = SportItem(
 user_id=User1.id, name="Riding Gear",
 description="Special helmet and trousers", sport=sport3)

session.add(sportItem3)
session.commit()


# Menu for Bench Ball
sport4 = Sport(user_id=User1.id, name="Bench Ball")

session.add(sport4)
session.commit()

sportItem1 = SportItem(
 user_id=User1.id, name="Bench",
 description="One on either end, used to stand on when you catch a ball.",
 sport=sport4)

session.add(sportItem1)
session.commit()

# Menu for Bench Ball
sport5 = Sport(user_id=User1.id, name="Skiing")

session.add(sport5)
session.commit()

sportItem1 = SportItem(
 user_id=User1.id, name="Skis",
 description="Attach to feet.", sport=sport5)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(
 user_id=User1.id, name="Helmet",
 description="Head protection", sport=sport5)

session.add(sportItem2)
session.commit()

sportItem3 = SportItem(
 user_id=User1.id, name="Goggles",
 description="Protection from sun, lots of reflection on snow.", sport=sport5)

session.add(sportItem3)
session.commit()

print "added sport items!"
