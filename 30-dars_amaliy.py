# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:24:47 2023

@author: Javohir
"""

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.name = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    def get_bosqich(self, yangi_bosqich):
        self.bosqich = yangi_bosqich     
    
    def set_bosqich(self):
        self.bosqich += 1
    
    def get_info(self):
        """Talaba haqida to'liq ma'lumot"""
        return f"Talaba {self.name} {self.familiya}  {self.bosqich} - bosqich talabasi "





class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni +=1
         
    def get_students(self):
        return [x.get_info() for x in self.talabalar ]




matem = Fan("Oliy matematika")
talaba1 = Talaba("Alijon", "Valiyev", 1995)
talaba2 = Talaba("Aliyev", "Baxodir", 1985)
talaba3 = Talaba("Olimov","Shokir", 1990)
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)


# AMALIY QISM

class Avto:
    def __init__(self, model, rang, karobka, yil):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.yil = yil
        self.km = 0
        self.avtolar = []
    def get_model(self):
        return self.model
    
    def get_info(self):
        return f"{self.rang.title()} {self.model} {self.yil} - yil {self.karobka} karobka"
    
    def add_avto(self, car):
        return self.avtolar.append(car)
    
    def set_model(self, model1):
        self.model = model1
    def get_cars(self):
        return [ x.get_info() for x in self.avtolar]
    def update_km(self):
         self.km +=1
    
avto = Avto("Molibu", "qora", "avtomat", 2023)
avto1 =Avto("Lacetti", "oq", "mexanik", 2018)
avto2 = Avto("matiz", "kulrang", "mexanik", 2013)
avto3 = Avto("Cobalt", "qizil", "avtomat", 2020)

avto.add_avto(avto)
avto.add_avto(avto1)
avto.add_avto(avto2)
avto.add_avto(avto3)

#print(avto.avtolar[1].get_info())
#print(avto.avtolar[0].get_info())
#print(avto.avtolar[2].get_info())
#print(avto.avtolar[3].get_info())

avto1.set_model('molibu')
print(avto1.get_info())

class Avtosalon:
    def __init__(self, nomi):
        self.nomi = nomi
        self.manzili = "Bag'dod"
        self.avtomobillar = []

    def add_avto(self, mobil):
        self.avtomobillar.append(mobil)

    def get_cars(self):
        return [ x.get_info() for x in self.avtomobillar]
salon = Avtosalon("AvtoUz")
salon.add_avto(avto)
salon.add_avto(avto1)
salon.add_avto(avto2)
salon.add_avto(avto3)
print(salon.get_cars())












    