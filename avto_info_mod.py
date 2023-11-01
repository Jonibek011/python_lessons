# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 12:49:35 2023

@author: LEGION
"""
def avto_info(kompaniya, model, rang, karobka, yil, narh=None):
    avto = {'kompaniya':kompaniya, 
            'model':model, 
            'rang':rang, 
            'karobka':karobka,
            'yil':yil,
            'narh':narh}
    return avto

def avto_kirit():
    print(" \nSaytimizdagi avtolar ro'yxatini shakllantiramiz")
    avtolar = []
    while True:
        kompaniya = input("Kompaniya nomini kiriting: ")
        model = input("Modelini kiriting: ")
        rang = input('Rangini kiriting: ')
        karobka = input('karobka: ')
        yil = input('Yilii kiriting: ')
        narh = input('narhini kiriting: ')
        avtolar.append(avto_info(kompaniya, model, rang, karobka, yil, narh))
        javob = input("Yana mashina qo'shishni istaysizmi yes/no")
        if javob == 'no':
           break
        return avtolar     
def avto_print(avto_info):
    """Avtomobillar haqida malumot saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['model'].upper()}, Karobka: {avto_info['karobka']}, Narhi: {avto_info['narh']}$" )