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
	return 'Hello, world!”'


@app.route('/mygames')
def getmygames():
    try:
        games = utilfunctions.makelist(client.games.export_by_player("titledKing23"))
        return games
    except requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})


app.run(port=5000)
