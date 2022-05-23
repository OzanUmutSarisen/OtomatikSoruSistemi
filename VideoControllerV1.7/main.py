#"C:\\Users\\ozanu\\OneDrive\\Masaüstü\\1 Saat Geri Sayım.mp4"
#Verileri almak için yazılmış python dosyaları
import MongoDB_Dowload
import MongoDB_Answer

#kodda kulanılan moduller
import cv2
import time
import math
import tkinter
from ffpyplayer.player import MediaPlayer

destroy = False  # Tuşabasıldığında cevap ekranının kapnması için
questionCount = 0  # soru sayaç


def start(number):
    global destroy
    global questionCount
    questionCount = 0
    stopPoint = 0  # kaç kere durdurduğumuzu içinde tutuyor
    arrStopTimes = MongoDB_Dowload.DowloadStopTimer()  # stoptimer programındaki durdurma zamanı verilerini alıyor
    arrQuestions = MongoDB_Dowload.DowloadQuestions()  # QuestionsAndAnswerMaker kodundaki "____" konularak oluşturulan soru cümlelerini ve cevapları alıyor



    player = MediaPlayer("ExampleVideo.mp4")#videonun ses kısmı
    time.sleep(2.6)
    cap = cv2.VideoCapture("ExampleVideo.mp4")#Bilgisyardan video dostasını çekme

    starTime = time.time()  # Programın çalışma süresinin başlangıcı(bununla videonun kaçıncı saniyesinde olduğubu öğreniyoruz)
    while True:
        time.sleep(0.015)  # videoyu normalde çok hızlı oynattığı için yavaşlatmak amacıyla
        # Capture frame-by-frame
        success, frame = cap.read()  # read the camera frame

        if not success:
            break
        else:

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            if StopTimeCalculater(stopPoint, arrStopTimes) == math.ceil(
                    time.time() - starTime):  # videoda soru geldiği zaman gerektiği yerde durmasını sağlıyor
                player.set_pause(5)
                screen = tkinter.Tk()  # soru için yeni bir ekran oluşturuyor
                screen.geometry()
                starTime2 = time.time()  # sorunun ne kadar ekranda kalacağını belirlemek için zamanlayıcı başlatıyor

                label = tkinter.Label(text=arrQuestions[stopPoint],
                                      font="arial 20")  # ekrana yazılacak soruyu ve kullanılacak yazı türünü puntosu ile belirtiyor
                label.grid(column=1, row=0)  # sorunun konumunu beliliyor

                metin = tkinter.Entry(screen, width=40)  # cavap yazıalcak alanı oluşturuyor
                metin.grid(column=1, row=2)  # cevap yaazılacak alanın yerini belirliyor

                browse_btn = tkinter.Button(screen, text="Send Answer", command=Destroy, repeatdelay=3, height=2,
                                            width=15)  # cavabı yollamak için buton oluşturuyor(command de buttona basıldığında ne yapılacağı beliritliyor)
                browse_btn.grid(column=1, row=5)  # butonun konumunu beeliriyor

                while 1:  # Soru sorma penceresini çaık tutma ve kodu çalışır tutmak için
                    if (time.time() - starTime2) > 10 or destroy:
                        AcceptAnswer(metin, screen, number)
                        break
                    screen.update()
                player.set_pause(0)
                stopPoint += 1
                starTime = time.time()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


def AcceptAnswer(metin, screen, number):  # Cevap gönderme butonu yazılan cevabı alıyor cevap yazılmazsada soru dolarsa boş cevap
    global questionCount
    questionCount = questionCount + 1
    MongoDB_Answer.Upload(question="questions" + str(questionCount), answer=metin.get(), studentNumber=number)  # Cevabı "MongoDB.pn" dosyanındaki "UploadAnswer" fonksiyonuna yolluyor
    screen.destroy()  # cevap ekranını kaldırmak için


def Destroy():  # Tuşa basıp cevabı yollayınca kapatmak için
    global destroy
    destroy = True


def StopTimeCalculater(stopCount, arrStopTimes):  # Videonun ne zmana duracağını hesaplıyor
    if stopCount == 0:
        return math.ceil(arrStopTimes[stopCount])
    elif stopCount == len(arrStopTimes) - 1:
        return math.ceil(arrStopTimes[stopCount])
    else:
        return math.ceil(arrStopTimes[stopCount] - arrStopTimes[stopCount - 1])

