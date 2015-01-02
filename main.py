import random
yarismacilarpuanlar = {}
ycilar = []
def kelimelistesi():
    kelimeler={"adrift" : "Hint: Loose","aground": "Hint: resting on the shore or bottom","astern":"Ipucu","ashore":"Ipucu","anchor":"Ipucu","freeboard":"Ipucu","buoy":"Ipucu","beam":"Ipucu","beacon":"Ipucu","brow":"Ipucu","draft":"Ipucu","embark":"Ipucu"}
    return kelimeler
def yarismacilar():
    global  yarismacilarpuanlar
    print "Yarismacilari girin"
    while 1:
        girdi =  raw_input(str(len(yarismacilarpuanlar)+1)+". Yarismacinin isimini giriniz:")
        if girdi in yarismacilarpuanlar.keys():
            print "Ayni isim daha once girilmis"
        yarismacilarpuanlar[girdi] = 0
        ycilar.append(girdi)
        if len(yarismacilarpuanlar) == 3:
            break
def yarisma():
    kelimeler=kelimelistesi()
    for sira in ycilar:
        print "Sira " + sira +" 'da. 5 Tahmin Hakkin Var.\n"
        tahminedilecek = random.choice(kelimeler.keys())
        print kelimeler[tahminedilecek]
        i = 0
        noktalar='_ ' *len(tahminedilecek)
        while i <= 5:
            print noktalar
            while 1:
                harf = raw_input("Harf: ")
                if len(harf) <2:
                    break
                else:
                    print "Harf Girmek Zorundasiniz"
            try:
                yer = tahminedilecek.index(harf)
                noktalar = noktalar[:yer*2] + harf + noktalar[yer*2+1:]
            except:
                pass
            i = i +1
        print "Harf tahmin hakkin doldu."
        if tahminedilecek == raw_input("Kelimeyi Tahmin Et "):
            print "Dogru Cevap\n"
            yarismacilarpuanlar[sira] = yarismacilarpuanlar[sira] + 25
        else:
            print "Yanlis Cevap.\n"
yarismacilar()
while 1:
    yarisma()
    print "Oyun sonu"
    for ycp in ycilar:
        print ycp+ " " +str(yarismacilarpuanlar[ycp])+ " Puanda."
    while 1:
        girdi = raw_input("Yeniden ? e/h\n")
        if girdi == "h" :
            cik = 1
            break
        elif girdi == "e":
            cik = 0
            break
        else:
            print "Yanlis girdi."
    if cik == 1:
        break
