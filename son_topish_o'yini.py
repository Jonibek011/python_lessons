# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:24:40 2023

@author: ADMIN
"""
import random 

def sontop(n=10):
    son = random.randint(1,n)
    print(f"Keling son topish o'yinini o'ynaymiz. Men 1 dan {n} gacha bo'lgan bir son o'yladim topa olasizmi? ")    
    taxminlar = 0
    while True:
        taxminlar +=1
        taxmin =int(input(">>>"))        
        if taxmin < son:
            print(f"Xato, men o'ylagan son {taxmin} dan kattaroq")
        elif taxmin > son:
            print(f"Xato men o'ylagan son {taxmin} dan kichikroq")
        else:
            break
    print(f"To'g'ri siz javobni {taxminlar} martada topdingiz!!!")
    return taxminlar 

def sontop_pc(n=10):
    input(f"Endi siz 1 dan {n} gacha son o'ylang men topaman, son o'ylagan bo'lsangiz istalgan tugmani bosing")    
    
    yuqori =n
    quyi = 1
    taxminlar = 0   
    
    while True:
        taxminlar +=1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin =quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t), men o'ylagan son bundan kattaroq (+),"
                      f"men o'ylagan son bundan kichikroq (-)")
        if javob == '+':
            quyi = taxmin+1
        elif javob == '-':
            yuqori = taxmin-1
        else:
            break
    print(f"Topdim, men {taxminlar} urinishda topdim!!! ")
    return taxminlar
    
def play(n=10):
    yana = True
    while True:
        taxminlar_user = sontop(n)
        taxminlar_pc = sontop_pc(n)
        if taxminlar_user > taxminlar_pc:
            print("Yutdim men kamroq urinishda topdim")
        elif taxminlar_user < taxminlar_pc:
            print("Yutdingiz siz kamroq urinishda topdingiz")
        else:
            print("Durrang!!!")
        yana = int(input("Yana o'ynaysizmi? ha(1)\yo'q(0):"))
        if yana == 0:
            break
        
            
       
        
        
        
    