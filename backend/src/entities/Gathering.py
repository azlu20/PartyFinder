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

class GatheringSchema(Schema):
    PartyID = fields.Number()
    HostID = fields.Number()
    Location = fields.String()