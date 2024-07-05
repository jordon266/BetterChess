import requests
import json
import time
import Constants

class APIHandler:    
    def __init__(self):
        self.headers  = {'Accept': 'application/x-ndjson','Authorization': f'Bearer {Constants.TOKEN}'}       
    def getallgamesbyuser(self,username,params):
        fullurl = Constants.URL+Constants.MAIN_API_ENDPOINT+Constants.GAMESBYUSER_ENDPOINT+username     
        response = requests.request("GET", url=fullurl, headers=self.headers,params=params)
        games= [json.loads(line, object_hook=dict) for line in response.text.splitlines()]
        return games
    
class SessionHandler:
    def __init__(self):
        self.s = requests.Session() 
    def login(self):
        data = f"------WebKitFormBoundary1mNByeI9bEiVtpDG\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n{Constants.UNAME}\r\n------WebKitFormBoundary1mNByeI9bEiVtpDG\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n{Constants.PWD}\r\n------WebKitFormBoundary1mNByeI9bEiVtpDG\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\n\r\n------WebKitFormBoundary1mNByeI9bEiVtpDG--\r\n"
        url = "https://lichess.org:443/login"
        return self.s.post(url=url,data=data,headers=Constants.SESSION_HEADER)
        
    def request_analysis(self,id):  
        request_analysis_url = f'https://lichess.org/{id}/request-analysis'
        return self.s.post(request_analysis_url, headers=Constants.SESSION_HEADER)
        
# Rewritten Test

# params = {'since':'true','until':'true', 'color':'true', 'analysed':'true', 'vs':'true','rated':'true','moves':'true','literate':'true','sort':'true'}
api_params = {'opening':'true', 'evals':'true'}
api = APIHandler()
gameslist = api.getallgamesbyuser(Constants.UNAME,api_params)
# ids = api.getidfromgames(gameslist)
# print(ids)
# s = SessionHandler(Constants.UNAME,Constants.PWD)
# print (s.login())
# num = 1
# for id in ids:
#     print(num)
#     print(s.request_analysis(id))
#     time.sleep(30)
#     num +=1 
# may move this to util functions
