
from .entities.entity import Session, engine, Base
from .entities.User import User

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

users = session.query(User).all()

testobj = User(2, "testFirst", "testLast", "NA", 19, "male", 1111111, 100)
session.add(testobj)
session.commit()
session.close()

users = session.query(User).all()
for user in users:
    print(f'({user.userID}) {user.firstName} - {user.lastName}')