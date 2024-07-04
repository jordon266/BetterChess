import requests
import json
import time
# get all my games

    # get games put into list
    # get id for each game and put into list
    # request analysis for each game
token ='lip_88V9PY5fawgJg6mBIVeM'
uname ='titledKing23'
password ='rT+Chv9BLpz)GRP'
gameslist = []
params = {'since':'true','until':'true', 'color':'true', 'analysed':'true', 'vs':'true','rated':'true','moves':'true','literate':'true','sort':'true'}
default_api_endpoint_params = 'opening=true&evals=true&clocks=true'

def api_getallgamesbyuser(username,token):  
    url = f'https://lichess.org/api/games/user/{username}?'     
    headers = {'Accept': 'application/x-ndjson','Authorization': f'Bearer {token}'}
    response = requests.request("GET", url+default_api_endpoint_params, headers=headers)
    games= [json.loads(line, object_hook=dict) for line in response.text.splitlines()]
    return games
            
def request_analysis(username,password):
    url = "https://lichess.org:443/login"
    
    headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary1mNByeI9bEiVtpDG", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Linux\"", "Accept": "*/*", "Origin": "https://lichess.org", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://lichess.org/login", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Priority": "u=1, i"}
    data = f"------WebKitFormBoundary1mNByeI9bEiVtpDG\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n{username}\r\n------WebKitFormBoundary1mNByeI9bEiVtpDG\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n{password}\r\n------WebKitFormBoundary1mNByeI9bEiVtpDG\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\n\r\n------WebKitFormBoundary1mNByeI9bEiVtpDG--\r\n"
    # get lila2 cookie for request-analysis
    session = requests.session() 
    r =  session.post(url, headers=headers, data=data)
    print(r)
    ids = getidfromgames(username=uname,token=token) 
    for id in ids:     
        request_analysis_url = f'https://lichess.org/{id}/request-analysis'
        resp = session.post(request_analysis_url, headers=headers)
        print(resp)
        time.sleep(35)
    print('done')
    
 
def getidfromgames(username,token):
    results =[]
    games=api_getallgamesbyuser(username,token)
    for game in games:
        if 'analysis' not in game:
            results.append(game['id'])
    return results



# Function below for debugging purposes 
def getallgamesinfo(username,token):
    gamesinfo = { 'totgames': 0, 'toteval': 0, 'totwhite': 0, 'totblack': 0,'blitznum' : 0, 'rapidnum': 0,  'classinum' : 0,'vscompnum' : 0,'vswhiteai' : 0, 'totwins': 0, 'totloss' : 0} 
    games = api_getallgamesbyuser(uname,token)
    username =''
    for game in games:
        if 'winner' in game:
            gamesinfo['totgames'] += 1
            if 'analysis' in game:
                gamesinfo['toteval'] += 1
            if game['speed'] == 'blitz':
                gamesinfo['blitznum'] += 1
            if game['speed'] == 'rapid':
                gamesinfo['rapidnum'] += 1
            if game['speed'] == 'classical':
                gamesinfo['classinum'] += 1
            if game['source'] == 'pool' or game['source'] == 'friend':
                if game['players']['white']['user']['name'] == username:
                    gamesinfo['totwhite'] +=1
                    if game['winner'] == 'white':
                        gamesinfo['totwins'] += 1
                    else:
                        gamesinfo['totloss'] += 1
                else:
                    gamesinfo['totblack'] +=1                    
                    if game['winner'] == 'black':
                        gamesinfo['totwins'] += 1
                    else:
                        gamesinfo['totloss'] += 1                  
            if game['source'] == 'ai':
                gamesinfo['vscompnum'] +=1
                if 'user' in game['players']['white']:
                    gamesinfo['totwhite'] += 1                   
                    if game['winner'] == 'white':
                        gamesinfo['totwins'] += 1
                    else:
                        gamesinfo['totloss'] += 1   
                else:
                    gamesinfo['totblack'] += 1               
                    if game['winner'] == 'white':
                        gamesinfo['totwins'] += 1
                    else:
                        gamesinfo['totloss'] += 1  
        else:
            print(game['id']) 
    return gamesinfo
            
            
            
            
            
        
    
            
    



ids = getidfromgames(username=uname,token=token) 
print(ids)
gameinfo = getallgamesinfo(username=uname,token=token)
print(gameinfo)  
request_analysis(uname,password=password)
gameinfo = getallgamesinfo(username=uname,token=token)

print(gameinfo)  

            
            