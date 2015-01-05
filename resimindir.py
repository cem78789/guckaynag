__author__ = 'ICY'
## Ismail Cem Yilmaz
## Resim indirici
from bs4 import BeautifulSoup
import httplib,os
import urllib2
class image:
    def __init__(self):
        self.icerik = ""
    def icerikcek(self,adres):
        self.adres = adres
        try:
            html = urllib2.urlopen("http://"+adres).read()
        except urllib2.HTTPError, err:
            print err
        self.icerik = html
        self.soup = BeautifulSoup(str(self.icerik))
    def corbabak(self):
        self.corbabak = []
        for tag in self.soup.find_all('img'):
            self.corbabak.append(tag.get('src'))
        return self.corbabak
    def resimindir(self,adres):
        baglan = httplib.HTTPConnection((adres.split('//')[-1]).split('/')[0])
        i = 0
        istenecek = (adres.split('/'))[3::]
        print( "/".join(istenecek))
        baglan.request('GET',"/"+"/".join(istenecek))
        gelen = baglan.getresponse()
        if gelen.reason == 'OK':
            print adres.split('/')[-1] + " Dosyasi istendi ve olumlu cevap alindi."
            yaz = open(adres.split('/')[-1],'wb')
            yaz.write(gelen.read())
            yaz.close()
            print adres.split('/')[-1] + " Dosyasi indirildi ve kaydedildi."
        else:
            print adres.split('/')[-1] +" Sunucu istenen dosyaya olumlu cevap vermedi."
    def resimkontrol(self,dosya):
        konum = os.getcwd()
        dosyalisetesi = os.listdir(konum)
        if dosya in dosyalisetesi:
            print dosya + " Dosyasi gecerli dizinde bulundugundan indirme listesine alinmadi."
            return 0
        else:
            print dosya + " Indirme listesine alindi."
            return 1
def calistir(site):
    resimler = []
    resim = image()
    resim.icerikcek(site)
    print ("Adresinden alinan verilerin islenmesine baslandi.")
    for a in  resim.corbabak():
        if a.startswith('http') and resim.resimkontrol(a.split('/')[-1]):
            resim.resimindir(a)




