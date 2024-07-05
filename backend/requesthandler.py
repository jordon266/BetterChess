import requests
import json
import time
import Constants

class APIHandler:    
    def __init__(self):
        self.url = 'https://lichess.org/api/'
        self.headers  = {'Accept': 'application/x-ndjson','Authorization': f'Bearer {Constants.TOKEN}'}       
    def getallgamesbyuser(self,username,params):
        endpoint = f'games/user/{username}?'  
        response = requests.request("GET", self.url+endpoint, headers=self.headers,params=params)
        games= [json.loads(line, object_hook=dict) for line in response.text.splitlines()]
        return games
# may move this to util functions
    def getidfromgames(self,listgames):
        idlist = []
        for game in listgames:
            if 'analysis' not in game:
                idlist.append(game['id'])
        return idlist
    
class SessionHandler:
    def __init__(self,uname,pword):
        self.s = requests.Session() 
        self.headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary1mNByeI9bEiVtpDG", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*", "Origin": "https://lichess.org", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://lichess.org/login", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Priority": "u=1, i"}

    def login(self):
        data = f"------WebKitFormBoundary1mNByeI9bEiVtpDG\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n{Constants.UNAME}\r\n------WebKitFormBoundary1mNByeI9bEiVtpDG\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n{Constants.PWD}\r\n------WebKitFormBoundary1mNByeI9bEiVtpDG\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\n\r\n------WebKitFormBoundary1mNByeI9bEiVtpDG--\r\n"
        url = "https://lichess.org:443/login"
        return self.s.post(url=url,data=data,headers=self.headers)
        
    def request_analysis(self,id):  
        request_analysis_url = f'https://lichess.org/{id}/request-analysis'
        return self.s.post(request_analysis_url, headers=self.headers)
        
# Rewritten Test

# params = {'since':'true','until':'true', 'color':'true', 'analysed':'true', 'vs':'true','rated':'true','moves':'true','literate':'true','sort':'true'}
api_params = {'opening':'true', 'evals':'true'}
api = APIHandler()
gameslist = api.getallgamesbyuser(Constants.UNAME,api_params)
ids = api.getidfromgames(gameslist)
print(ids)
s = SessionHandler(Constants.UNAME,Constants.PWD)
print (s.login())
num = 1
for id in ids:
    print(num)
    print(s.request_analysis(id))
    time.sleep(30)
    num +=1 
