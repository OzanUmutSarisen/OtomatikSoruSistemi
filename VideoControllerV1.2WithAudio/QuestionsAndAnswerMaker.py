
import MongoDB

def Quest():
    data = MongoDB.DowloadData()#MongoDB kodununun DowloadData Fonksiyonu aracılığı ile mongodv deki datayı alıyor

    arrQuestions = []#boş array sorular için
    arrAnswers = []#boş array cevaplar için

    for line in data:
        if "<S>" in line["line"]:#soru olan lineları tespit ediyor
            a = line["line"].find("<S>")  # cevabın başlangıcını buluyor
            b = line["line"].find("</S>") + 4  # cevabın sonunu buluyor
            answer = line["line"][a:b]  # cavabı sonundaki ve başındaki işaretlerle alıyor
            arrQuestions.append(line["line"].replace(answer, "________"))  # sorudan cavabı sonundaki ve başındaki işaretlerle silip arraye ekliyor
            arrAnswers.append(line["line"][a + 3:b - 4])  # cevabı başında ve sonunda işaretler olmadan arraye ekliyor

    return arrQuestions, arrAnswers