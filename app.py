# -*- coding: utf-8 -*-
from flask import Flask, render_template
import json, requests
from functions import *

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/calcNoiseLevel')
def calcNoiseLevel(): 
    
    incoming =  reqRefStruct('INCOMING')[0]
    valid =  reqRefStruct('VALID')[0]
  
    noiseLvl = round( incoming/valid * 100, 1)

    out = {
    'incoming':incoming, 'valid': valid, 'noiseLvl':noiseLvl
    }

    return out
    

@app.route('/getIncomingTable')
def getIncomingTable():
	buff = extractIncomingData()
	return buff

if __name__ == "__main__":
    app.run(debug=True)