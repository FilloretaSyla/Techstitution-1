from flask import Blueprint, render_template, request
from bson import json_util
from app import mongo

mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="GET":
        return render_template("indexi.html")
    elif request.method=="POST":
        data = request.form.to_dict()
        return json_util.dumps(data)
    else:
        return "bad request"


@mod_main.route('/<string:id>', methods=['GET', 'POST'])
def get_doc(id):
    db = mongo.db.arkep

    if request.method=="GET":
        doc = db.find({"_id":Objectid(id)})
    	#doc_json = json_util.dumps(doc)
	#return render_template('doc.html', doc_json )
	return render_template('doc.html', doc = doc )
	
    else:
        return "bad request"

@mod_main.route('/lista', methods=['GET'])
def lista():
   dokumentat = mongo.db.arkep.find()
   return render_template('lista.html', dokumentat = dokumentat)
