# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:38:44 2023

@author: LEGION
"""
#telefonlar = {"Anvar":"GALAXY XS", "Sarvar":"Iphonr XS", "Botir":'Redmi note 10 pro'}
#for k, q in telefonlar.items():
#    print(f"{k} ning telefoni {q}")
    
    #keys( metodi)
#mevalar = {"olma":10000, \
# "anor":12000, \
 #    "anjir":15000, "o'rik": 18000}
#print(mevalar.keys())
#print("Do'kondagi maxsulotlar")
#for meva in mevalar.keys():
#    print(meva)
#mahsulotlar = {'olma':10000, "anor":15000, 'nok':12000, 'shaftoli':18000}
#bozorlik = ["olma", "nok", "baliq", "kalbasa"]
#print("Do'konda bor mahsulotlar")
#for mahsulot in mahsulotlar.keys():
     
     #print(mahsulot.title())
 # if mahsulot in bozorlik:
  #    print(f"{mahsulot} : {mahsulotlar[mahsulot]}")
#for bozor in bozorlik:
#    if bozor not in mahsulotlar:
 #      print(f"Iltomos do'koningizga {bozor} ham olib keling")
        
       #Maxsulotlarni ketma ketlikda chiqarish
#for mahsulot in sorted(mahsulotlar):
 #   print(mahsulot)

#              values()
 
#print(mahsulotlar.values())
#print("Do'konimizda quyidagi narhlar mavjud")
#for mahsulot in mahsulotlar.values():
 #   print(mahsulot)
 

#         AMALIY MASHG"ULOT
python_lugat = {".py":"python fayllar belgisi", "upper()":"barcha harflarni katta qilib chiqaradi", \
"len":"ro'yxat uzunligini o'lchaydi", "lower()":"Barcha harflarni kichik qilib chiqaradi", \
"set":"ro'yxatdagi takrorlanga qismlarni olib tashlaydi", \
"rstrip":"ro'yxat oxiridagi bo'shliqni olib tashlaydi", \
"del": "ro'yxatdagi elementlarni indeks orqali o'chiradi", \
"range":"O'ziga yuklangan sonlarni birin ketin consulga chiqaradi"}
#for python, lugat in python_lugat:
#print(python_lugat.keys())
#print(python_lugat.values())
#for a in python_lugat:
    #  print(f"{a} : {python_lugat[a]}")
   
    
#davlatlar = {"o'zbekiston":"toshkent", "usa":"vashington", "india":"munbai", "france":"paris"}
#davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz \n>>>").lower()
#poytaxt = davlatlar.get(davlat)
#if davlat == None:
#    print("kecirasiz bizda bunday davlat mavjud emas")
#elif davlat == "usa":
 #   print(f"{davlat.upper()} ning poytaxti {poytaxt.title()}")
#else:
#    print(f"{davlat.title()}ning poytaxti {poytaxt.title()} ")


dokon = {"olma":10000, "anor":8000, "nok":17000, "sabzi":3000, "yog'":21000, "baliq":46000}
bozorlik = ["o'rik", "banan", "baliq", "yog'", "sabzi"]
#for doc in dokon:
    #if doc in bozorlik:
     #   print(f"{doc} : {dokon[doc]}")
    #if doc not in bozorlik:
        #print(f"Iltimos, {doc} ham olib kelinglar")
haridor = input("Salom, siz qaysi maxsulotni sotib olmoqchisiz")
doc = dokon.get(haridor)
if haridor in dokon:
    print(f"{haridor} : {doc}")        
else:
    print("Afsuski bizda bunday maxsulot mavjud emas")
     
     