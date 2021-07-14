from .entities.entity import Session, engine, Base
from .entities.User import User, UserSchema
from flask import Flask, jsonify, request
from flask_cors import CORS
# generate database schema
Base.metadata.create_all(engine)

# start session
app = Flask(__name__)
CORS(app)

@app.route('/user')
def get_users():
    session = Session()
    users_temp = session.query(User).all()
    schema = UserSchema(many=True)
    users = schema.dump(users_temp)
    session.close()

    return jsonify(users)


@app.route('/user/add', methods=['POST'])
def add_users():
    session = Session()
    added_user = UserSchema().load(request.get_json())
    user = User(added_user.data)
    # userID = request.form.get("userID")
    # firstName = request.form.get("firstName")
    # lastName = request.form.get("lastName")
    # location = request.form.get("location")
    # age = request.form.get("age")
    # gender = request.form.get("gender")
    # phoneNumber = request.form.get("phoneNumber")
    # partyFiendRating = request.form.get("partyFiendRating")
    # print(userID)
    # print(firstName)
    # users = User(userID, firstName, lastName, location, age, gender, phoneNumber, partyFiendRating)
    session.add(user)
    session.commit()
    schema = UserSchema
    session.close()
    userjson = schema.dump(user.data)
    print(user.data)
    return jsonify(userjson)
# users = session.query(User).all()

# testobj = User(2, "testFirst", "testLast", "NA", 19, "male", 1111111, 100)
# session.add(testobj)
# session.commit()
# session.close()

# users = session.query(User).all()
# for user in users:
#     print(f'({user.userID}) {user.firstName} - {user.lastName}')
