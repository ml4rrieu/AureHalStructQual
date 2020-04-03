import requests, json

def reqRefStruct(state, fl='') : 
    iduvsq = 81173
    url = 'https://api.archives-ouvertes.fr/ref/structure/?rows=1000&wt=json\
    &q=parentDocid_i:81173&fq=valid_s:'+state+fl
    
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
    structDict = {}
    
    for i in range(len( halResult[1])): # get the list form HAL API
        struct = halResult[1][i]
        structDict[i] = {}
        structDict[i]['name'] = struct['label_s'] 
        structDict[i]['docid'] = struct['docid'] 
        structDict[i]['nb'] = reqHal(struct['docid'])

        #shortcur date format
        date = struct['updateDate_tdate']
        structDict[i]['date'] = date[ : date.index('T')]
        
        # if i == 5 : break
    

    return structDict

    
    