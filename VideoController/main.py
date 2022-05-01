#"C:\\Users\\ozanu\\OneDrive\\Masaüstü\\1 Saat Geri Sayım.mp4"
#Verileri almak için yazılmış python dosyaları
import StopTimer
import QuestionsAndAnswerMaker

#kodda kulanılan moduller
import cv2 as cv
import time
import math
import tkinter

cap = cv.VideoCapture("ExampleVideo.mp4")#Bilgisyardan video dostasını çekme
starTime = time.time()#Programın çalışma süresinin başlangıcı(bununla videonun kaçıncı saniyesinde olduğubu öğreniyoruz)
stopPoint = 0 #kaç kere durdurduğumuzu içinde tutuyor
arrStopTimes = StopTimer.StopTimer()#stoptimer programındaki durdurma zamanı verilerini alıyor
arrQuestions, arrAnswers = QuestionsAndAnswerMaker.Quest()#QuestionsAndAnswerMaker kodundaki "____" konularak oluşturulan soru cümlelerini ve cevapları alıyor
destroy = False
#print(arrStopTimes)

def AcceptAnswer(): #Cevap gönderme butonu yazılan cevabı alıyor cevap yazılmazsada soru dolarsa boş cevap
    print(metin.get())
    screen.destroy()

def Destroy(): #Tuşa basıp cevabı yollayınca kapatmak için
    global destroy
    destroy = True

def StopTimeCalculater(stopCount): #Videonun ne zmana duracağını hesaplıyor
    if stopCount == 0:
        return math.ceil(arrStopTimes[stopCount])
    elif stopCount == len(arrStopTimes)-1:
        return math.ceil(arrStopTimes[stopCount])
    else:
        return math.ceil(arrStopTimes[stopCount]-arrStopTimes[stopCount-1])


while cap.isOpened(): # videonun açık kalmasını ve üzerinde işlemler yapabilmemizi sağlıyor
    destroy = False
    time.sleep(0.023) # videoyu normalde çok hızlı oynattığı için yavaşlatmak amacıyla
    ret, frame = cap.read() #videodan 2 tane geri dönüt alıyor(açıklaması çok uzun)

    if not ret: # videonun olup olmadığına bakıyor
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv.imshow("TezProject", frame)#video penceresi oluşturuyor
    if cv.waitKey(1) == ord('q'):# q tuşuna basınca videodan çıkışı sağlıyor
        break

    #print(StopTimeCalculater(stopPoint), math.ceil(time.time() - starTime))

    if StopTimeCalculater(stopPoint) == math.ceil(time.time() - starTime):#videoda soru geldiği zaman gerektiği yerde durmasını sağlıyor
        screen = tkinter.Tk() #soru için yeni bir ekran oluşturuyor
        screen.geometry()
        starTime2 = time.time() #sorunun ne kadar ekranda kalacağını belirlemek için zamanlayıcı başlatıyor

        label = tkinter.Label(text=arrQuestions[stopPoint], font="arial 20") #ekrana yazılacak soruyu ve kullanılacak yazı türünü puntosu ile belirtiyor
        label.grid(column=1, row=0)#sorunun konumunu beliliyor

        metin = tkinter.Entry(screen, width=40)#cavap yazıalcak alanı oluşturuyor
        metin.grid(column=1, row=2)#cevap yaazılacak alanın yerini belirliyor

        browse_btn = tkinter.Button(screen, text="Send Answer", command=Destroy, repeatdelay=3, height=2, width=15)#cavabı yollamak için buton oluşturuyor(command de buttona basıldığında ne yapılacağı beliritliyor)
        browse_btn.grid(column=1, row=5)#butonun konumunu beeliriyor

        while 1:#Soru sorma penceresini çaık tutma ve kodu çalışır tutmak için
            if (time.time() - starTime2) > 10 or destroy:
                AcceptAnswer()
                break
            screen.update()

        stopPoint += 1
        starTime = time.time()

cv.destroyAllWindows()#video bitince ekranı kapatmak için
