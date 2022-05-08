import pymongo

def UploadData(dataSource = "StopTheVideo.txt", dataClient = "test", dataBase = "test"):
    try:
        file = open(dataSource)

    except FileNotFoundError:
        print("The file not found")
        exit()

    client = pymongo.MongoClient("mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/test?retryWrites=true&w=majority")
    db = client[dataClient]
    collection = db[dataBase]

    a = 0
    for line in file:
        post = {"_id": a, "time": line[0:8], "line": line[10:-1]}
        a = a+1
        collection.insert_one(post)

def DowloadData(dataClient = "test", dataBase = "test"):

    client = pymongo.MongoClient("mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/test?retryWrites=true&w=majority")
    db = client[dataClient]
    collection = db[dataBase]
    data = collection.find({})
    return data

def DeleteData(dataClient = "test", dataBase = "test"):
    client = pymongo.MongoClient("mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/test?retryWrites=true&w=majority")
    db = client[dataClient]
    collection = db[dataBase]
    collection.delete_many({})


def UploadAnswer(dataClient = "test", dataBase = "answer", studentNumber = "2018555055", question="", answer=""):
    client = pymongo.MongoClient("mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/test?retryWrites=true&w=majority")
    db = client[dataClient]
    collection = db[dataBase]
    #post = {"_id": studentNumber, "Question": question, "Answer": answer}
    collection.update_one({"_id": "2018555055"}, {"$set": {question: answer}})

