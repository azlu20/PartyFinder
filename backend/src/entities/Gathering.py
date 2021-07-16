from sqlalchemy.sql.expression import null, true
from sqlalchemy.sql.schema import ForeignKey
from .entity import Base
from sqlalchemy import create_engine, Column, String, Integer
from marshmallow import Schema, fields

class Gathering(Base):
    __tablename__ = 'Gatherings'
    PartyID = Column(Integer, primary_key=True)
    HostID = Column(Integer, ForeignKey('Users.userID'))
    Location = Column(String, nullable = True)
    

    def __init__(self, partyID, hostID, location):
        self.PartyID = partyID
        self.HostID = hostID
        self.Location = location

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