# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:06:54 2023

@author: LEGION
"""

# 16 dars NESTING
car0 = {"marka":"malibu", "rang":"oq", "yil":"2020"}
car1 = {"marka":"lacetti", "rang":'qora', "yil":'2019'}
car2 = {"marka":"matiz", "rang":"kulrang", "yil":"2013"}
#print(f"{car0['marka']},  {car0['rang']}, {car0['yil']}")
#print(f"{car1['marka']},  {car1['rang']}, {car1['yil']}")
#print(f"{car2['marka']},  {car2['rang']}, {car2['yil']}")
 
# Bu usulni sal osonlashtiramiz

car = car0 #car = car1, car = car2
#print(f"{car['marka']},  {car['rang']}, {car['yil']}")
# Bu usulning kamchiligi har 3 ta avtomobil ma'lumotlarini bir vaqtda chiqarib berolmaydi
#Endi yana ham osonlashtiramiz
cars = [car0, car1, car2]
#for car in cars:
  #  print(f"{car['marka']},  {car['rang']}, {car['yil']}")

malibus = []
for n in range(10):
    new_cars = {"marka":"malibu", 
                "rang":None,
                "yil":"2022",
                "narh":None,
                "km":"0",
                "karobka":"avtomat"}
    malibus.append(new_cars)
#print(malibus)
#for malibu in malibus[:3]:
#    malibu['rang'] = 'qizil'

   # print(malibu)
 
#for malibu in malibus[3:6]:
#    malibu['rang'] = 'qora'
   # print(malibu)
   
#for malibu in malibus[6:]:
#    malibu['rang'] = 'kulrang'
#    malibu['karobka'] = 'mexanika'
    #print(malibu)
#for malibu in malibus:
   # print(malibu)
   
#for malibu in malibus:
#    if malibu["karobka"] == "avtomat":
#        malibu['narh'] = 40000
#    else:
 #       malibu['narh'] = 35000
#for malibu in malibus:
 #   print(malibu)
dasturchilar = {'ali':['python', 'c++'],
                'vali':['html','css', 'js'],
                "hasan":['php', 'sql'],
                'husan':['c++','c#']}
#for ism, tillar in dasturchilar.items():
    #print(f"{ism.title()} quyidagi dasturlash tillarini biladi:")
    #for til in tillar:
   #     print(til.upper())
hamkasblar = {'ali':{"familiya":"valiyev",
                     "tyil":1995,
                     "malumot":"oliy",
                     "tillar":['python', 'c++']},
              'vali':{"familiya":"rasulov",
                      "tyil":2002,
                      "malumot":"oliy",
                      "tillar":["html", "c++"]},
              'hasan':{"familiya":"yunusov",
                       "tyil":1993,
                       "malumot":"o'rta",
                       "tillar":['python', 'html']}}
for ism,info in hamkasblar.items():
    print(f"{ism.title()} {info['familiya'].title()} {info['tyil']} - yilda yug'ilgan.\n Ma'lumoti: {info['malumot']},"
          f" Quyidagi dasturlash tillarini biladi")
    for til in info['tillar']:
        print(til.upper())
   
   
   
   
   
   
   
   