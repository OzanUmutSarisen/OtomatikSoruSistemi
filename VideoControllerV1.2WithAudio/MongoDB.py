import pymongo

def UploadData(dataSource = "StopTheVideo.txt", dataClient = "test", dataBase = "test"):# Öğretmenin girmiş olduğu soru/alt yazı dosyasını MongoDB ye upload etmek için
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

def DowloadData(dataClient = "test", dataBase = "test"):#Upload edilmiş datayı alabilmek için

    client = pymongo.MongoClient("mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/test?retryWrites=true&w=majority")
    db = client[dataClient]
    collection = db[dataBase]
    data = collection.find({})
    return data

def DeleteData(dataClient = "test", dataBase = "test"):#Bir datanın içini silebilmek için
    client = pymongo.MongoClient("mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/test?retryWrites=true&w=majority")
    db = client[dataClient]
    collection = db[dataBase]
    collection.delete_many({})


def UploadAnswer(dataClient = "test", dataBase = "answer", studentNumber = "2018555055", question="", answer=""):#öğrencinin vermiş olduğu cevabı MongoDB ye upload edebilmek için
    client = pymongo.MongoClient("mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/test?retryWrites=true&w=majority")
    db = client[dataClient]
    collection = db[dataBase]
    collection.update_one({"_id": studentNumber}, {"$set": {question: answer}})
