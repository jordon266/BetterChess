import requesthandler

def getidfromgames(listgames):
    idlist = []
    for game in listgames:
        if 'analysis' not in game:
            idlist.append(game['id'])
    return idlist