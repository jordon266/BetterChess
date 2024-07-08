from flask import Flask
from flask import jsonify
from flask import Response
import requesthandler
import Constants
# import  utilfunctions
app = Flask(__name__)
api = requesthandler.APIHandler()

@app.route('/mygames') 
def home():
    try:
        api_params = {'opening':'true'}
        return Response(api.getallgamesbyuser(Constants.UNAME,api_params).iter_lines(), mimetype='application/json')
    except requesthandler.requests.exceptions.RequestException as e:
        return jsonify({"error":str(e)})

# @app.route('/mygames/blitz')
# def myblitzgames(): 
#     try:
#         api_params = {'opening':'true','perfType':'rapid'}
#         return api.getallgamesbyuser(Constants.UNAME,api_params)
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error":str(e)})

# @app.route('/mygames/rapid')
# def myrapidgames():
#     try:
#         api_params = {'opening':'true','perfType':'rapid'}
#         return api.getallgamesbyuser(Constants.UNAME,api_params)
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error":str(e)})

# @app.route('/mygames/white')
# def mywhitegames():
#     try:
#         api_params = {'opening':'true','color':'white'}
#         return api.getallgamesbyuser(Constants.UNAME,api_params)
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error":str(e)})
    
# @app.route('/mygames/black')
# def myblackgames():
#     try:
#         api_params = {'opening':'true','color':'black'}
#         return api.getallgamesbyuser(Constants.UNAME,api_params)
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error":str(e)})

# @app.route('/mygames/datedesc')
# def mywins():
#     try:
#         api_params = {'opening':'true', 'evals':'true','sort':'dateDesc'}
#         return api.getallgamesbyuser(Constants.UNAME,api_params)
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error":str(e)})

# @app.route('/mygames/dateasc')
# def mylosses():
#     try:
#         api_params = {'opening':'true', 'evals':'true','sort':'dateAsc'}
#         return api.getallgamesbyuser(Constants.UNAME,api_params)
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error":str(e)})
app.run(port=5000)
