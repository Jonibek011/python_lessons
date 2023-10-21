# -*- coding: utf-8 -*- 
"""
Created on Wed Oct 18 10:01:39 2023

@author: ADMIN
"""
#ism =input("Salom, ismingiz nima? \n>>")
#savol = f"Slom {ism.title()} yoshingiz nechida \n>"
#yosh = input(savol)
#yosh = int(yosh)
#weight = input("Vazningiz necha kg ? \n")
#weight = float(weight)

#son = 1
#while son<=5:
 #  print(son, end=' ')
 #   son = son+1
#print("dastur tugadi")

#print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
#savol = "Istalgan sonni kiriting"
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing) \n"
#qiymat = ' '
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat) ** 2)
#    else:
#        print("Dastur yakunlandi")
  # ISHORA      
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
#savol = "Istalgan sonni kiriting"
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing) \n"
#qiymat = ' '
#ishora = True
#while ishora :
 #   qiymat = input(savol)
 #   if qiymat == 'exit':
 #       ishora = False
 #   else:
 #       print(float(qiymat) ** 2)
        
#print("Daastur yakunlandi")

# BREAK
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
#savol = "Istalgan sonni kiriting"
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing) \n"
#qiymat = ' '
#while True:
 #   qiymat = input(savol)
 #   if qiymat == 'exit':
 #       break
  #  else:
 #       print(float(qiymat) ** 2)
#print("Dastur yakunlandi")
    
#sonlar = list(range(1,11))
#for son in sonlar:
   # if son == 5:
  #    break
 #   print(f"{son} ning kvadrati {son ** 2} ga teng")
    
 # CONTINUE
#sonlar = list(range(1,11))
#for son in sonlar:
  #  if son == 5:
 #       continue
#    print(f"{son} ning kvadrati {son ** 2} ga teng")


#son = 0
#while son <10:
#    son +=1
#    if son%2==0:
  #      continue
#    else:
#        print(son)

# Amaliy qism

#savol = "Sevimli kitoblaringizni kiriting"
#savol += "(barcha kitoblarni kiritib bo'lgach 'stop deb yozing) \n"
#while True:
  #  kitob = input(savol)
  #  if kitob == 'stop':
 #       break
#print('Raxmat')

print('Chiptngizni oling')
savol = "necha yosh uchun chipta olmoqchisiz(so'rovni tugatgach 'exit' yoki 'quit' deb yozing) \n>>"
while True:
    qiymat = input(savol)
    
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    if yosh <7:
        narh = 2000
    elif 7<= yosh <18:
        narh = 3000
    elif 18 <= yosh < 65:
        narh = 10000
    else:# 65 <= yosh:
        narh = 0
    if narh == 0:
        print("Sizga chipta bepul")
    else:
        print(f"Siz uchun chiptaning narxi {narh} so'm")
        
        
        




























