# Functions to help with parsing object returned by api
import datetime

# Make Generator Object into List
def makelist(games):
    gameslist = []
    for game in games:  #gAssuming the function is named export_by_player
        print(game)
        gameslist.append(game)
    return gameslist
