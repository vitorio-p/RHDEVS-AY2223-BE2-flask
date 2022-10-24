from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db

app = Flask(__name__)

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")

# Write your flask code here

# GET / homepage that returns a welcome message 
@app.route("/", methods = ["GET"])
def hello_world():
    return "welcome to vito's scrappy website"


@app.route("/profiles/<user_id>", methods = ["GET"])
def user(user_id):
    # GET /{id} to retrieve the name and all scores of a profile 
    return db[int(user_id)]

'''

@app.route("/profiles/<user_id>", methods = ["GET", "POST", "DELETE"])
def user(user_id):

    # GET /{id} to retrieve the name and all scores of a profile 
    if request.method == "GET":
        return db[int(user_id)]
    
    # POST /profiles to create a new profile (name only) 
    if request.method == "POST":
        name = flask.request.values.get('name')

    # DELETE /{id} to delete a profile 
    if request.method == "DELETE":
        return "2"

    # catch-all
    else:
        return "go back"
'''

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)