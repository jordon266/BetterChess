# Functions to help with parsing object returned by api
import datetime
from flask import Flask, jsonify
import json

# load json file into variable
def loadfile(fname):
    with open(fname,'r') as f:
        data = json.load(f)     
    f.close()
    return data 

# Make Generator Object into List
def makelist(games):
    gameslist = []
    for game in games:  
        # print(game)
        gameslist.append(game)
    return gameslist

# Takes a List turns it into a string and organizes it so that it can be used in a json fileclea
def prettyprint(obj):
    with open('games.json', 'w') as f:
        f.write(jsonify(obj).data.decode('utf-8'))
    f.close()

# Gets All Games from json file
def getgames():
    data = loadfile('games.json')     
    return data

# Gets All Games from json file based on speed
def getgames(speed):
    blitzgames = []
    data = loadfile('games.json')     
    for val in data:
        if val['speed'] == speed:
            blitzgames.append(val)
    return blitzgames