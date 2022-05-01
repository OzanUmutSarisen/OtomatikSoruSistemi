
def StopTimer():
    try:
        file = open("StopTheVideo.txt")#data dosyasını alma

    except FileNotFoundError:
        print("The file not found")
        exit()

    arrLineTimes = []#boş array soru olan linelardaki zaman için
    arrStops = []#boş array datadaki zamanı düzenleyip tutmak için

    for line in file:
        if "<S>" in line:
            times = line[:8]#doya türüne göre değişir ilk 8 karakteri almak için
            lineTime = 0#o line ın zamanı hesaplamak için
            count = 6#saat dakika ve saniye düzeninde 6 karakter olduğu için 00:00:00 6 tane 0
            for a in times.replace(":", ""):#":" karakteri hariç tüm değerleri döndürmek için
                if count == 6:#10 ve fazla saat
                    lineTime = lineTime + (int(a) * 10 * 3600)
                elif count == 5:#tek basamaklı saat
                    lineTime = lineTime + (int(a) * 3600)
                elif count == 4:#çift basamaklı dk
                    lineTime = lineTime + (int(a) * 10 * 60)
                elif count == 3:#tek basamaklı dk
                    lineTime = lineTime + (int(a) * 60)
                elif count == 2:#çift basamaklı sn
                    lineTime = lineTime + (int(a) * 10)
                elif count == 1:#tek basamklı sn
                    lineTime = lineTime + (int(a))
                count = count - 1

            arrLineTimes.append(lineTime)#değerleri stop dostasına eklmek


    for i in range(0, len(arrLineTimes)):#2 metnin başlangıç sürelerinden sorunun ne zaman ekrana geleceğini hesaplıyor
        if i == (len(arrLineTimes)-1):
            newStop = arrLineTimes[i]+5
        else:
            newStop = (arrLineTimes[i]+arrLineTimes[i+1])/2

        arrStops.append(newStop)

    file.close()
    return arrStops
