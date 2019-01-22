FYI this version works for cancer

**PatientSys**

PatientSys,hastalarin tedavi gorme siralarini yapay zeka ile daha ileri tasiyarak durumu kritik olan ve ilerleyen zamanlarda olabilecek hastalari tespit edip onlara oncelik veren bir paket programidir. PatientSys ile bir cok hastanin hayatini kurtarip ve bir cok hastaninda tedavi bekleme sureclerini kisaltarak tedavi bekleme surecindeki acilarina son verip, bu surecte olusabilecek yeni hastaliklarin onune geciyor ve hali hazirda bulunan hastaliga erken mudahele etme firsatini yakaliyoruz.

In the United Kingdom, 70,000 patients are waiting on surgery. 9,600 of these patients have already waited more than a year. This waiting can be a disaster for critical patients and future critical patients. Their sickness will be bad or they will be dead at this waiting. PatientSys is sorting patients by the urgency with machine learning thus saving people lives

PatientSys Presentation,

https://docs.google.com/presentation/d/1yxPaGNI5aUjwMM8_bHnz3M3_mRgSjO5jTxel-qW_gcU/edit?usp=sharing

**Kullanim/Usage**

>Online Demo

http://bit.ly/patientsys



>Desktop App


Hali hazirda bir sunucu uzerinde calismakta olan PatientSys programini, repo'yu `clone` ettikten sonra `clone` ettigimiz klasore girip terminal uzerinden;

It's already working on a server. You only need to clone or download the repository then write this code's to terminal in a local directory of a repository;

```
cd Electron
npm install
npm run start
```

**Frameworkler/Frameworks**

>Makine Ogrenmesi/Machine Learning

Makine ogrenmesi kullaniminda `numpy`, `matplotlib` frameworkleri kullanilmistir

In machine learning usage, I used `numpy`, `matplotlib` frameworks

Train Dataset: 

Physical Dataset: https://docs.google.com/spreadsheets/d/1Sa6qt0SwqokViqVQwXap5eoH4BrxcZOKZXxswQTs4p8/edit#gid=0

Factors Dataset: https://docs.google.com/spreadsheets/d/13f18Qc6hzw4-RN94PeLewM5PTiDrruWpdJGf_kZRvas/edit#gid=0


>Back-End

Back-End kisminda `LEMP` sunucu uzerinde `PHP` ile calisilmistir.

I worked in `PHP` on `LEMP` server

>Fron-End

AJAX icin `jQuery` kullanildi

Used `jQuery` for AJAX

>Desktop App

`Electron.JS` ile bu sorunun ustesinden gelinmistir

Worked with `Electron.JS`


**Liste Ekrani Veri Anlamlari/List Screen Meaning**

Veriler v0.1 versiyonu oldugu icin ve demo esnasinda ogrenim suresini uzatmamasi icin genelleme yapilarak saklanmaktadir
In this demo version values are rounded

>Yas/Age

0.15 = (Between) 0-15 (Yas Arasi)     

0.30 = (Between) 15-30 (Yas Arasi)

0.45 = (Between) 30-45 (Yas Arasi)

0.60 = (Between) 45-60 (Yas Arasi)

0.75 = (Between) 60-75 (Yas Arasi)

0.90 = (Between) 90-105 (Yas Arasi)

1.00 = (105 and higher) (105 ve Uzeri)


>Kilo/Weight

0.25 = (Between) 0-25 (Arasi)

0.50 = (Between) 25-50 (Arasi)

0.75 = (Between) 50-75 (Arasi)

1.00 = (Between and higher) 75-100 (Arasi ve Uzeri)


>Hastalik ve Fizik Ortalamasi Hakkinda/About Sickness Avg, Physic Avg

Bu iki veri yapay zeka tarafindan kisinin onceki vakalara goz onunda bulundurularak ne kadar kritik oldugunu gosteren verilerdir. Hastalik ortalamasi, Hastalik ortalamasi, vucut ortalamasi ile birlikte hesaplanip kisinin hastalik ortalamasini gosterir. Fizik ortalamasi ise vucudunun ne kadar kuvvetli oldugunu ya da ne kadar zayif oldugunu anlamada yardimci olmaktadir. Dusuk sayilar bu veriler icin iyilik gostergesidir. 

This two value is predicting by machine learning. Machine learning comparing patient data and old patient data are then It's predicting an urgency for the patient. Sickness Avg predicting with Physic Avg. Physic(It means Body, sorry for my language) Average is predicted resistance of patient's body. Low Sickness Avg means good but low Physic Avg means bad.


>Spor, Sigara, Alkol, Aile Gecmisi Hakkinda/About Sports, Tobacoo, Alcohol, Family History

1 pozitif 0 negatif anlamlarina gelmektedir

1 means positive 0 means negative.





