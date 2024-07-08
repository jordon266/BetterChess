import requests
import Constants

class APIHandler:    
    def __init__(self):
        self.headers  = {'Accept': 'application/x-ndjson','Authorization': f'Bearer {Constants.TOKEN}'}       
    def getallgamesbyuser(self,username,params):
        fullurl = Constants.URL+Constants.MAIN_API_ENDPOINT+Constants.GAMESBYUSER_ENDPOINT+username     
        return requests.request("GET", url=fullurl, headers=self.headers,params=params,stream=True)

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