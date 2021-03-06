from __future__ import print_function
from sqlalchemy.sql import schema

from sqlalchemy.sql.expression import true
from .entities.Gathering import Gathering, GatheringSchema
import sys
from .entities.entity import Session, engine, Base
from .entities.User import User, UserSchema
from flask import Flask, json, jsonify, request
from flask_cors import CORS

# generate database schema
Base.metadata.create_all(engine)

# start session
app = Flask(__name__)
CORS(app)


# @app.route('/user/<int:id>', methods=['GET'])
# def get_users(id):
#     session = Session()
#     if id == 0 or id is None:
#         users_temp = session.query(User).all()
#     else:
#         users_temp = session.query(User).filter_by(userID=id).all()
#     schema = UserSchema(many=True)
#     users = schema.dump(users_temp)
#     session.close()
#     return jsonify(users)


# @app.route('/user/add', methods=['POST'])
# def add_users():
#     session = Session()
#     schema = UserSchema()
#     jsonuser = request.get_json(silent=True)
#     user = schema.load(jsonuser)
#     print(user.firstName, file = sys.stderr)
#     # userID = request.form.get("userID")
#     # firstName = request.form.get("firstName")
#     # lastName = request.form.get("lastName")
#     # location = request.form.get("location")
#     # age = request.form.get("age")
#     # gender = request.form.get("gender")
#     # phoneNumber = request.form.get("phoneNumber")
#     # partyFiendRating = request.form.get("partyFiendRating")
#     # print(userID)
#     # print(firstName)
#     # users = User(userID, firstName, lastName, location, age, gender, phoneNumber, partyFiendRating)
#     session.add(user)
#     session.commit()
    
#     session.close()
#     return 2
# # users = session.query(User).all()

# # testobj = User(2, "testFirst", "testLast", "NA", 19, "male", 1111111, 100)
# # session.add(testobj)
# # session.commit()
# # session.close()

# # users = session.query(User).all()
# # for user in users:
# #     print(f'({user.userID}) {user.firstName} - {user.lastName}')

# @app.route('/party/<int:id>', methods =['GET'])
# def get_party(id):
#     session = Session()
#     if id != None or id != 0:
#         gathering_temp = session.query(Gathering).all()
#     else:
#         gathering_temp = session.query(Gathering).filter_by(PartyID=id).all()
#     schema = GatheringSchema(many=true)
#     gatherings = schema.dump(gathering_temp)
#     session.close()
#     return jsonify(gatherings)

object_map = {
    "user" : User,
    "gathering" : Gathering
}
schema_map ={
     "userschema" : UserSchema,
    "gatheringschema" : GatheringSchema   
}
@app.route('/<string:object>/<int:id>', methods = ['GET'])
def get(object, id):
    session = Session()
    if id != None or id != 0:
        object_temp = session.query(object_map.get(object)).all()
    else:
        object_temp = session.query(object_map.get(object)).all()
    schemastring = object + "schema"
    schema = schema_map.get(schemastring)(many=true)
    object = schema.dump(object_temp)
    session.close()
    return jsonify(object) 