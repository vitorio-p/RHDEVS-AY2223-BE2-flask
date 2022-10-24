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

if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)