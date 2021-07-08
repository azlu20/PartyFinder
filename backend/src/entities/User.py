from .entity import Base
from sqlalchemy import create_engine, Column, String, Integer


class User(Base):
    __tablename__ = 'Users'
    userID = Column(String, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    location = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    phonenumber = Column(Integer)
    partyfiendrating = Column(Integer)

    def __init__(self, userID, firstname, lastname, location, age, gender, phonenumber, partyf):

        self.userID = userID
        self.location = location
        self.age = age
        self.gender = gender
        self.partyfiendrating = partyf
        self.phonenumber = phonenumber
        self.firstName = firstname
        self.lastName = lastname

    def findMutualFriends(self, friendObj):
        mutualfriends = []
        for ele in self.friendsID:
            if (friendObj.friendsID == ele):
                mutualfriends.append(ele)
