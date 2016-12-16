from flask import Blueprint, render_template, request
from bson import json_util
from app import mongo

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET', 'POST'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    if request,method=="GET":
        return render_template("indexi.html")
    elif request.method=="POST":
        data = request.form.to_dict()
	mongo.db.arkep.insert(data)
        return json_util.dumps(data)
    else
        return "bad request"

    #db=mongo.db.arkep.insert({"emri":"ipko"})


@mod_main.route('/ardita', methods=['GET', 'POST'])
def index1():
    ''' Renders the App index page.
    :return:
    '''
    if request,method=="GET":
        return render_template("ardita.html")
    elif request.method=="POST":
        data = request.form.to_dict()
	mongo.db.arkep.insert(data)
        return json_util.dumps(data)
    else
        return "bad request"
