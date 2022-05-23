import pymongo
client = pymongo.MongoClient("mongodb+srv://natsu:1234@cluster0.idnat.mongodb.net/?retryWrites=true&w=majority")

def Upload(dataClient = "AudienceProvoker", dataBase = "Answers", studentNumber = "2018555055", lesson="InToMachineLe", video="Video0", question="", answer=""):#öğrencinin vermiş olduğu cevabı MongoDB ye upload edebilmek için

    global client
    db = client[dataClient]
    collection = db[dataBase]
    if not(collection.find_one({"_id": studentNumber})):
        post = {"_id": studentNumber}
        collection.insert_one(post)

    quest = lesson + "." + video + "." + question
    post = {quest: {"answer": answer}}
    collection.update_many({"_id": studentNumber}, {"$set": post})