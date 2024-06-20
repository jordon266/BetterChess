from flask import Flask, jsonify
import requests
import os
import berserk
import  utilfunctions

app = Flask(__name__)
apikey = os.environ['lichesskey']
session = berserk.TokenSession(apikey)
client = berserk.Client(session=session)



@app.route('/') # ‘https://www.google.com/‘
def home():
    try:
        games = utilfunctions.makelist(client.games.export_by_player("titledKing23"))
        utilfunctions.prettyprint(games)
        return "games accessed"
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})
    return  "Test"

@app.route('/myblitzgames')
def myblitzgames():
    try:    
        return utilfunctions.getgames('blitz')
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})

@app.route('/myradidgames')
def myrapidgames():
    try:    
        return utilfunctions.getgames('rapid')
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})

app.run(port=5000)
