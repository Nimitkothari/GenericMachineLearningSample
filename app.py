from flask import Flask,jsonify,request,Response
from flask import request
import json
import pickle
import os
port = int(os.getenv("PORT", 3000))
app = Flask(__name__)
#For Price
linReg1 = pickle.load(open('predict1.pkl', 'rb'))
#For Bedrooms
linReg2 = pickle.load(open('predict2.pkl', 'rb'))
#For Size
linReg3 = pickle.load(open('predict3.pkl', 'rb'))
#For Age
linReg4 = pickle.load(open('predict4.pkl', 'rb'))
#For Bathrooms
linReg5 = pickle.load(open('predict5.pkl', 'rb'))
print('after model loaded')

@app.route('/predictSize', methods=['POST'])
def predict_size():
    try:
        req_body = request.get_json(force=True)
        param1 = req_body['Bedrooms']
        param2 = req_body['Age']
        param3 = req_body['Bathrooms']
        param4 = req_body['Price']
        pred = linReg3.predict([[param1, param2, param3,param4]])
        result = pred[0]
        msg = {
                "Predicted size is": "%s" % (result)
            }
        resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
@app.route('/predictPrice', methods=['POST'])
def predict_price():
    try:
        req_body = request.get_json(force=True)
        param1 = req_body['Size']
        param2 = req_body['Bedrooms']
        param3 = req_body['Age']
        param4 = req_body['Bathrooms']
        pred = linReg1.predict([[param1, param2, param3,param4]])
        result = pred[0]
        msg = {
                "Predicted Price is": "%s" % (result)
            }
        resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
@app.route('/predictBedrooms', methods=['POST'])
def predict_bedrooms():
    try:
        req_body = request.get_json(force=True)
        param1 = req_body['Size']
        param2 = req_body['Age']
        param3 = req_body['Bathrooms']
        param4 = req_body['Price']
        pred = linReg2.predict([[param1, param2, param3,param4]])
        result = pred[0]
        msg = {
                "Predicted Bedrooms are": "%s" % (result)
            }
        resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
@app.route('/predictAge', methods=['POST'])
def predict_age():
    try:
        req_body = request.get_json(force=True)
        param1 = req_body['Size']
        param2 = req_body['Bedrooms']
        param3 = req_body['Bathrooms']
        param4 = req_body['Price']
        pred = linReg4.predict([[param1, param2, param3,param4]])
        result = pred[0]
        msg = {
                "Predicted Age ": " is %s" % (result)
            }
        resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
@app.route('/predictBathrooms', methods=['POST'])
def predict_bathrooms():
    try:
        req_body = request.get_json(force=True)
        param1 = req_body['Size']
        param2 = req_body['Bedrooms']
        param3 = req_body['Age']
        param4 = req_body['Price']
        pred = linReg5.predict([[param1, param2, param3,param4]])
        result = pred[0]
        msg = {
                "Predicted Bathrooms are": "%s" % (result)
            }
        resp = Response(response=json.dumps(msg),
                            status=200,\
                            mimetype="application/json")
        return resp
    except Exception as e:
        print(e)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
