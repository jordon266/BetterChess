import requesthandler

# def getidfromgames(listgames):
#     idlist = []
#     for game in listgames:
#         if 'analysis' not in game:
#             idlist.append(game['id'])
#     return idlist

# api_params = {'opening':'true', 'evals':'true'}
# api = requesthandler.APIHandler()
# gameslist = api.getallgamesbyuser(requesthandler.Constants.UNAME,api_params)
# ids = getidfromgames(gameslist)
# print(ids)
# s = requesthandler.SessionHandler()
# print (s.login())

# num = 1
# for id in ids:
#     print(num)
#     print(s.request_analysis(id))
#     requesthandler.time.sleep(35)
#     num +=1 


# Rewritten Test

params = {'since':'true','until':'true', 'color':'true', 'analysed':'true', 'vs':'true','rated':'true','moves':'true','literate':'true','sort':'true'}

# api = APIHandler()
# print(api.getallgamesbyuser(Constants.UNAME,params=params))