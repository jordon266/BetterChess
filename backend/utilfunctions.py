# Functions to help with parsing object returned by api
import datetime

# Make Generator Object into List
def makelist(games):
    gameslist = []
    for game in games:  
        print(game)
        gameslist.append(game)
    return gameslist
