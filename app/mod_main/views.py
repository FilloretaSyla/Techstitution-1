import os
from flask import Blueprint, render_template, request, redirect, url_for
from app import mongo
from bson import json_util, ObjectId
from os.path import join, dirname, realpath
from app import upload_folder

mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET','POST'])
def index():
    db = mongo.db.arkep
    if request.method == 'GET':
        return render_template('index.html')

@mod_main.route('/upload')
def upload_files():
   return render_template('upload.html')

@mod_main.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    db = mongo.db.arkep
    emriOperatorit = request.values.get('1-1-EmriNdermarrsit')
    directory = str(upload_folder) + emriOperatorit
    if not os.path.exists(directory):
        os.makedirs(directory)
    if request.method == 'POST':
        f1 = request.files['file1']
        f1.save(os.path.join(upload_folder,f1.filename))
        f1.save(os.path.join(directory, f1.filename))
        f2 = request.files['file2']
        f2.save(os.path.join(directory,f2.filename))
        f3 = request.files['file3']
        f3.save(os.path.join(directory,f3.filename))
        data = request.form.to_dict()
        db.insert(data)
        return redirect(url_for('.listo'))
#
# @mod_main.route('/<path:filen>')
# def file_download(filen):
#     db = mongo.db.arkep
#     filena= db.find_one({"5-1-KopjeCertifikatesBiz":filen})
#     return url_for('upload_folder',filename='Diamanti/'+filen)

@mod_main.route('/operatoret',methods=['GET'])
def listo():
    db = mongo.db.arkep
    myCursor = db.find();
    if request.method == 'GET':
        return render_template('list.html', myCursor=myCursor)

@mod_main.route('/operatoret/<string:op>',methods=['GET'])
def op_view(op):
    db = mongo.db.arkep
    operatori = db.find_one({"1-1-EmriNdermarrsit":op})
    if request.method == 'GET':
        return render_template('operatori.html', operatori=operatori)
    else:
        return 'bad request'

@mod_main.route('/operatoret/delete_document<id>')
def delete_document(id):
    db = mongo.db.arkep
    db.remove({"_id":ObjectId(id)})
    return redirect(url_for('.listo'))
