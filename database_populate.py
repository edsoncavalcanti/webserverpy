from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base,Restaurant,MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


#Add values to db
myFirstRestaurant = Restaurant(name="Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
chessepizza = MenuItem(name="Cheese Pizza",description="made with chesse",course="Entree",price="$8.99",restaurant=myFirstRestaurant)
session.add(chessepizza)
session.commit()
session.query(MenuItem).all()

#Read values from db

items = session.query(Restaurant).all()


for item in items:
    print(item.name)