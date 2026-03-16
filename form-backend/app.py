from flask import Flask, request, jsonify
import json
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
uri=os.getenv("MONGO_URL")
client=MongoClient(uri,server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db=client.form_data
    collection=db['users']  
except Exception as e:
    print(e)

app= Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page"

@app.route('/submit', methods=['post'])
def submit():
    data=request.json
    uname=data['name']
    pword=data['password']
    collection.insert_one({"name":uname,"password":pword})
    print(uname,pword)
    return jsonify({"message":"Data received succesfully!","user":uname})

@app.route('/view',methods=['get'])
def view():
    all_data=collection.find()
    users_det=list(all_data)
    for user in users_det:
        user.pop('_id')
    return jsonify(users_det)

@app.route('/search',methods=['post'])
def search():
    data=request.json
    uname=data['name']
    user_det=list(collection.find({"name":uname}))
    for user in user_det:
        user.pop('_id')
    return jsonify(user_det)


if __name__== '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')