
def Quest():
    try:
        file = open("StopTheVideo.txt")

    except FileNotFoundError:
        print("The file not found")
        exit()

    arrLines = []#boş array soru olan linelar için
    arrQuestions = []#boş array sorular için
    arrAnswers = []#boş array cevaplar için

    for line in file:
        if "<S>" in line:#soru olan lineları tespit ediyor
            arrLines.append(line[10:-1])

    for line in arrLines:
        a = line.find("<S>")#cevabın başlangıcını buluyor
        b = line.find("</S>")+4#cevabın sonunu buluyor
        answer = line[a:b]#cavabı sonundaki ve başındaki işaretlerle alıyor
        arrQuestions.append(line.replace(answer, "________"))#sorudan cavabı sonundaki ve başındaki işaretlerle silip arraye ekliyor
        arrAnswers.append(line[a+3:b-4])#cevabı başında ve sonunda işaretler olmadan arraye ekliyor

    file.close()
    return arrQuestions, arrAnswers