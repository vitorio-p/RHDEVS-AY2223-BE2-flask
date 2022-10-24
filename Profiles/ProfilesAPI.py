from flask import Blueprint
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@app.route("/profiles/<id>", methods = ["GET", "POST", "DELETE"])
def user(user_id):

    # GET /{id} to retrieve the name and all scores of a profile 
    if request.method == "GET":
        return db[int(user_id)]