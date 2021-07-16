from .entity import Base
from sqlalchemy import create_engine, Column, String, Integer
from marshmallow import Schema, fields

class User(Base):
    __tablename__ = 'Users'
    userID = Column(String, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    location = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    phoneNumber = Column(Integer)
    partyFiendRating = Column(Integer)

    def __init__(self, userID, firstname, lastname, location, age, gender, phoneNumber, partyfiendrating):

        self.userID = userID
        self.location = location
        self.age = age
        self.gender = gender
        self.partyfiendrating = partyfiendrating
        self.phoneNumber = phoneNumber
        self.firstName = firstname
        self.lastName = lastname

    def findMutualFriends(self, friendObj):
        mutualfriends = []
        for ele in self.friendsID:
            if (friendObj.friendsID == ele):
                mutualfriends.append(ele)

class UserSchema(Schema):
    userID = fields.Number()
    firstName = fields.String()
    lastName = fields.String()
    location = fields.String()
    age = fields.Number()
    gender = fields.String()
    phoneNumber = fields.Number()
    partyFiendRating = fields.Number()