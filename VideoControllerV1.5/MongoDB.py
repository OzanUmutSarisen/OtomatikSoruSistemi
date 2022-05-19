import pymongo
from StopTimer import StopTimeFinder
from QuestionsAndAnswerMaker import Quest


client = pymongo.MongoClient("mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/?retryWrites=true&w=majority")


def UploadData(dataSource = "StopTheVideo.txt", dataClient = "AudienceProvoker", dataBase = "Lessons", lesson="InToMachineLe", Video = "Video0"):# Öğretmenin girmiş olduğu soru/alt yazı dosyasını MongoDB ye upload etmek için

    try:
        file = open(dataSource)

    except FileNotFoundError:
        print("The file not found")
        exit()

    global client
    db = client[dataClient]
    collection = db[dataBase]

    a = 1

    if not(collection.find_one({"_id": lesson})):
        collection.insert_one({"_id": lesson})

    for line in file:
        quest = Video + ".Quest" + str(a)
        post = {quest: {"time": line[0:8], "line": line[10:-1]}}
        a = a + 1
        collection.update_many({"_id": lesson}, {"$set": post})




def DeleteData(dataClient = "AudienceProvoker", dataBase = "Lessons"):#Bir datanın içini silebilmek için

    global client
    db = client[dataClient]
    collection = db[dataBase]
    collection.delete_many({})


def UploadAnswer(dataClient = "AudienceProvoker", dataBase = "Answers", studentNumber = "2018555055", lesson="InToMachineLe", video="Video0", question="", answer=""):#öğrencinin vermiş olduğu cevabı MongoDB ye upload edebilmek için

    global client
    db = client[dataClient]
    collection = db[dataBase]
    if not(collection.find_one({"_id": studentNumber})):
        post = {"_id": studentNumber}
        collection.insert_one(post)

    quest = lesson + "." + video + "." + question
    post = {quest: {"answer": answer}}
    collection.update_many({"_id": studentNumber}, {"$set": post})

def StopTime(dataClient = "AudienceProvoker", dataBase = "Lessons", lesson="InToMachineLe", video = "Video0"):

    global client
    db = client[dataClient]
    collection = db[dataBase]
    stopTimes = StopTimeFinder()
    if collection.find_one({"_id": lesson}):
        a = 1
        for x in stopTimes:
            quest = video + "StopTimers." +str(a)
            post = {quest: x}
            collection.update_many({"_id": lesson}, {"$set": post})
            a = a+1

def UploadQuest(dataClient = "AudienceProvoker", dataBase = "Lessons", lesson="InToMachineLe", video = "Video0"):

    global client
    db = client[dataClient]
    collection = db[dataBase]
    arrQuestions, arrAnswers = Quest()
    if collection.find_one({"_id": lesson}):
        a = 1
        for x in arrQuestions:
            quest = video + "Questions." + str(a)
            post = {quest: x}
            collection.update_many({"_id": lesson}, {"$set": post})
            a = a + 1
        a = 1
        for x in arrAnswers:
            quest = video + "Answers." + str(a)
            post = {quest: x}
            collection.update_many({"_id": lesson}, {"$set": post})
            a = a + 1
