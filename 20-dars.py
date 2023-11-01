# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:19:56 2023

@author: LEGION
"""

#def avto_info(zavod, model, rang, karobka, yil, narh = None):
 #   avto = {'zavod':zavod,
 #           'model':model,
 #           'rang':rang,
#            'karobka':karobka,
 #           'yil':yil,
#            'narh':narh}
 #   return avto
#avto1 = avto_info('Gm', 'molibu', 'qora', 'avtomat', 2023)
#avto2 = avto_info('GM', 'gentra', 'oq', 'avtomat', 2020, 16000)
 
#print("Avtosalonimizdagi avtolar ro'yxatini shakllantiramiz")
#avtolar = []
#while True:
 #   print(" \n Quyidagi malumotlarni kiriting:", end = '')
 #   zavod = input("Ishlab chiqaruvchi: ")
  #  model = input('Modeli: ')
  #  rang = input("Rangi: ")
  #   karobka = input("Karobkasi: ")
 #   yil = input("Ishlab chiqarilgan yili: ")
#    narh = input("Narhi: ")
 #   avtolar.append(avto_info(zavod, model, rang, karobka, yil, narh ))
 #   javob = input("Yanaavto qo'shishni istaysizmi? 'yes' or 'no'")
 #   if javob =='no':
#        break
##print(" \n Salonimizdagi avtolar")
#for avto in avtolar:
 #   if avto['narh']:
#        narh = avto['narh']
 #   else:
#        narh = 'Nomalum'
#    print(f"{avto['rang']} {avto['model']}, {avto['karobka']} karobka, Narhi: {narh}")

#def foydalanuvchi_info(ism, familiya, t_yil, t_joy, t_raqam, e_manzil):
 #   user = {'ism':ism,
 #           'familiya':familiya,
 #3           't_yil':t_yil,
# 3           't_joy':t_joy,
 #           't_raqam':t_raqam,
 #           'e_manzil':e_manzil}
#    return user
#foydalanuvchi = []
#while True:
 #   print("Salom, ma'lumotlaringizni kiriting; ")
#    ism = input("\n Ismingiz nima?: ")
 #   familiya = input("Familiyangizni kiriting; ")
 #   t_yil = input("Tug'ilgan yilingizni kiriting: ")
 #   t_joy = input("Tug'ilgan manzilingizni kiriting: ")
#    t_raqam = input("Telefon raqamingizni kiriting; ")
 #   e_manzil = input("Elektron pochta  manzilingizni kiriting: ")
    
 #   foydalanuvchi.append(foydalanuvchi_info(ism, familiya, t_yil, t_joy, t_raqam, e_manzil))
 #   javob = input("Yana ma'lumot kiritishni xoxlaysizmi ha\yoq")
##    if javob == 'yoq':
    #  break
#print("\nSizning ma'lumotlaringiz")
#for info in foydalanuvchi:
 #   print(f"{info['ism']} {info['familiya']} {info['t_yil']} - yilda {info['t_joy']} da tug'ilgan. e_manzili {info['e_manzil']}, telefon raqami {info['t_raqam']}")

def katta_son(a,b,c):
     max = a
     if b >= max:
         max = b
     if c >= max:
        max = c
     return max
kattasi = katta_son(1, 2, 3)
print(kattasi)
         

















