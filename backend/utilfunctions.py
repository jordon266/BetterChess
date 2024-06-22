# Functions to help with parsing object returned by api
import datetime
from flask import Flask, jsonify
import json
import os
import berserk



class utils:
    def __init__(self):
        # empty list
        self.mygames = []
        # name of app
        self.app = Flask(__name__)
        # apikey
        self.apikey = os.environ['lichesskey']
        #use api key to set session
        self.session = berserk.TokenSession(self.apikey)
        # use session to create a client
        self.client = berserk.Client(session=self.session)
        # get generator object returned by export players
        self.genobj = self.client.games.export_by_player("titledKing23")
        # turn genobj into list
        for game in self.genobj:
            self.mygames.append(game)
            
     # gets all games       
    def getallgames(self):    
        return self.mygames
    
    # get games by speed 
    def getgamesbyspeed(self, speed): 
        gamesbyspeed = []
        for val in self.mygames:
            if val['speed'] == speed:
               gamesbyspeed.append(val)
        return gamesbyspeed
    # get games by color and username
  
    def getgamesbycolor(self, color,name):
        games = []
        for game in self.mygames:
              # some game objects dont hav user in their so have to account for that
            if 'user' in game['players'][color]:
                if game['players'][color]['user']['name'] == name:
                    print(game['players'][color]['user']['name'] )
                    games.append(game)
                print(game)   
        return games

