**PatientSys**

PatientSys,hastalarin tedavi gorme siralarini yapay zeka ile daha ileri tasiyarak durumu kritik olan ve ilerleyen zamanlarda olabilecek hastalari tespit edip onlara oncelik veren bir paket programidir. PatientSys ile bir cok hastanin hayatini kurtarip ve bir cok hastaninda tedavi bekleme sureclerini kisaltarak tedavi bekleme surecindeki acilarina son verip, bu surecte olusabilecek yeni hastaliklarin onune geciyor ve hali hazirda bulunan hastaliga erken mudahele etme firsatini yakaliyoruz.

**Kullanim**

Hali hazirda bir sunucu uzerinde calismakta olan PatientSys programini, repo'yu `clone` ettikten sonra `clone` ettigimiz klasore girip terminal uzerinden;
```
cd Electron
npm install
npm run start
```
kodlarini yazarak calistirabilirsiniz. Calistirdiktan sonra sizi karsilayan `Landing Page` uzerinden veritabanina hasta girisi yapabilir ardindan girisini yaptiginiz hastalarin aciliyet durumuna gore siralanmis haline `List` sayfasi uzerinden erisebilirsiniz
**Frameworkler**

>Yapay Zeka

Yapay zeka kullaniminda `numpy`, `matplotlib` frameworkleri kullanilmistir

Yapay Zeka Egitim Verisi (Train Dataset): 

Physical Dataset: https://docs.google.com/spreadsheets/d/1Sa6qt0SwqokViqVQwXap5eoH4BrxcZOKZXxswQTs4p8/edit#gid=0

Factors Dataset: https://docs.google.com/spreadsheets/d/13f18Qc6hzw4-RN94PeLewM5PTiDrruWpdJGf_kZRvas/edit#gid=0


>Back-End

Back-End kisminda `LEMP` sunucu uzerinde `PHP` ile calisilmistir.
>Fron-End

Front-End gelistirme kisminda `jQuery` kullanilmistir
>Masaustu Uygulamasi

`Electron.JS` ile bu sorunun ustesinden gelinmistir

**Liste Ekrani Veri Anlamlari**

Veriler v0.1 versiyonu oldugu icin ve demo esnasinda ogrenim suresini uzatmamasi icin genelleme yapilarak saklanmaktadir

>Yas

0.15 = 0-15 Yas Arasi     

0.30 = 15-30 Yas Arasi

0.45 = 30-45 Yas Arasi

0.60 = 45-60 Yas Arasi

0.75 = 60-75 Yas Arasi

0.90 = 90-105 Yas Arasi

1.00 = 105 ve Uzeri


>Kilo

0.25 = 0-25 Arasi

0.50 = 25-50 Arasi

0.75 = 50-75 Arasi

1.00 = 75-100 Arasi ve Uzeri


>Hastalik ve Fizik Ortalamasi (Sickness Avg, Physic Avg)

Bu iki veri yapay zeka tarafindan kisinin onceki vakalara goz onunda bulundurularak ne kadar kritik oldugunu gosteren verilerdir. Hastalik ortalamasi, Fizik yani vucut ortalamasi ile birlikte hesaplanip kisinin hastalik ortalamasini gosterir. Fizik ortalamasi ise vucudunun ne kadar kuvvetli oldugunu ya da ne kadar zayif oldugunu anlamada yardimci olmaktadir. Dusuk sayilar bu veriler icin iyilik gostergesidir. 


>Spor, Sigara, Alkol, Aile Gecmisi

Bu veriler hastanin spor yapip yapmadigini ailesinde gecmis zamanlarda kanser olan ya da kanserden hayatini yitiren olup olmadiginin tutuldugu alanlardir. 1 pozitif 0 negatif anlamlarina gelmektedir



