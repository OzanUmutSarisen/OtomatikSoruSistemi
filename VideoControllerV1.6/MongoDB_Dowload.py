import pymongo

client = pymongo.MongoClient(host="localhost", port=27017)

def DowloadData(dataClient = "AudienceProvoker", dataBase = "Lessons", lesson="InToMachineLe", Video = "Video0"):#Upload edilmiş datayı alabilmek için

    global client
    db = client[dataClient]
    collection = db[dataBase]
    data = collection.find_one({"_id": lesson})
    return data[Video]

def DowloadStopTimer(dataClient = "AudienceProvoker", dataBase = "Lessons", lesson="InToMachineLe", Video = "Video0"):#Upload edilmiş datayı alabilmek için

    global client
    db = client[dataClient]
    collection = db[dataBase]
    data = collection.find_one({"_id": lesson})

    arr = []
    a = 1
    for x in data[Video+"StopTimers"]:
        arr.append(data[Video+"StopTimers"][str(a)])
        a = a + 1
    return arr

def DowloadQuestions(dataClient = "AudienceProvoker", dataBase = "Lessons", lesson="InToMachineLe", Video = "Video0"):#Upload edilmiş datayı alabilmek için

    global client
    db = client[dataClient]
    collection = db[dataBase]
    data = collection.find_one({"_id": lesson})
    arr = []
    a = 1
    for x in data[Video+"Questions"]:
        arr.append(data[Video+"Questions"][str(a)])
        a = a+1
    return arr
