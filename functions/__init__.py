from flask import jsonify
import requests, json


myStructId = 81173

def reqRefStruct(state, fl='') : 
    
    url = 'https://api.archives-ouvertes.fr/ref/structure/?rows=1000&wt=json\
    &q=parentDocid_i:'+str(myStructId)+'&fq=valid_s:'+state+fl
    # print(url)
    r = requests.get(url)
    r = r.json()
    #print(json.dumps(r,indent=4))
    num = r['response']['numFound']
    buff = []
    if num > 0: buff = r['response']['docs']
    return [num,buff]


def reqHal(structId) : 
    url = 'https://api.archives-ouvertes.fr/search/?rows=0&wt=json&fq=structId_i:'+str(structId)
    # print(url)
    r = requests.get(url)
    r = r.json()
    #print(json.dumps(r,indent=4))
    num = r['response']['numFound']
    return num


def extractIncomingData():
    halResult = reqRefStruct('INCOMING', '&fl=docid,updateDate_tdate,label_s')
    dataArray = []
    
    for i in range(len( halResult[1])): # get the list form HAL API
        struct = halResult[1][i]
        name = struct['label_s'] 
        docid = struct['docid'] 
        nb = reqHal(struct['docid'])
        date = struct['updateDate_tdate']
        date = date[ : date.index('T')] #shortcut date format
        
        dataArray.append([name, docid, nb, date])
             
        # if i == 5 : break #for debugging limit to few items

    return jsonify(dataArray)
