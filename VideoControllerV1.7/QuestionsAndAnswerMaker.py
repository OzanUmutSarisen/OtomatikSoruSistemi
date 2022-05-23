
import MongoDB_Dowload

def Quest():
    data = MongoDB_Dowload.DowloadData()#MongoDB kodununun DowloadData Fonksiyonu aracılığı ile mongodv deki datayı alıyor

    arrQuestions = []#boş array sorular için
    arrAnswers = []#boş array cevaplar için
    b=1

    for line in data:
        quest = "Quest" + str(b)
        if "<S>" in data[quest]["line"]:#soru olan lineları tespit ediyor
            answerS = data[quest]["line"].find("<S>")  # cevabın başlangıcını buluyor
            answerF = data[quest]["line"].find("</S>") + 4  # cevabın sonunu buluyor
            answer = data[quest]["line"][answerS:answerF]  # cavabı sonundaki ve başındaki işaretlerle alıyor
            arrQuestions.append(data[quest]["line"].replace(answer, "________"))  # sorudan cavabı sonundaki ve başındaki işaretlerle silip arraye ekliyor
            arrAnswers.append(data[quest]["line"][answerS + 3:answerF - 4])  # cevabı başında ve sonunda işaretler olmadan arraye ekliyor
        b = b + 1

    return arrQuestions, arrAnswers
