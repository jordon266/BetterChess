from flask import Flask, jsonify
import requests
import os
import berserk
import  utilfunctions

app = Flask(__name__)
apikey = os.environ['lichesskey']
session = berserk.TokenSession(apikey)
client = berserk.Client(session=session)
data = utilfunctions.utils()


@app.route('/') # ‘https://www.google.com/‘
def home():
    try:
        return data.getallgames()
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})
    return  "Test"

@app.route('/myblitzgames')
def myblitzgames():
    try:   
        return data.getgamesbyspeed('blitz')
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})

@app.route('/myrapidgames')
def myrapidgames():
    try:    
        return data.getgamesbyspeed('rapid')
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})

@app.route('/mywhitegames')
def mywhitegames():
    try:    
        return data.getgamesbycolor('white','titledKing23')
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})
    
@app.route('/myblackgames')
def myblackgames():
    try:    
        return data.getgamesbycolor('black' ,'titledKing23')
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})

@app.route('/allwins')
def mywins():
    try:    
        return data.getgamesbycolor('black' ,'titledKing23')
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})

app.run(port=5000)
