# 18- dars while
#print("Keling do'stlaringiz ro'yxatini tuzamiz")
#dostlar = []
#n=1

#while True:
 #   savol = f"{n} - do'stingiz ismini kiriting"
  #  ism = input(savol)
  #  dostlar.append(ism.title())
 #   takrorlash =input( "Yana ism kiritishni xoxlaysizmi? (ha/yo'q) \n>")
   # n += 1
    #if takrorlash != 'ha':
     #   break
#print("Sizning do'stlaringiz")
#for dost in dostlar:
#    print(dost)

#print("Do'stlaringiz yoshini saqlaymiz! ")
#dostlar = {}
#ishora = True
#while ishora:
#   ism = input("Dostingizning ismini kiriting: ")
#    yosh = input("Do'stingizning yoshini kiriting: ")
#    dostlar[ism] = int(yosh)
#    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q')")
#    if javob == "yo'q":
#        ishora = False
#print("Do'stlaringiz haqida ma'lumot")    
#for ism, yosh in dostlar.items():
#    print(f"{ism.title()} ning yoshi {yosh} da ")


#cars = ['nexia', 'matiz', 'bugatti', 'nexia', 'molibu', 'nexia']
#while 'nexia' in cars:
 #   cars.remove('nexia')
#print(cars)

#talabalar = ['olim', 'aziz', 'furqat', 'yaxyo']
#baholangan_talabalar = {}
#while talabalar:
 #   talaba = talabalar.pop()
#    baho = input(f"{talaba.title()} ning bahosini kiriting: ")
#    print("Talaba baholandi")
#    baholangan_talabalar[talaba] = int(baho)
    
    # Amaliy mashg'ulot
#print("Assalomu alaykum, sahifamizga hush kelibsiz! \nNima buyurtma qilmoqchisiz")
#buyurtmalar = []
#ishora = True
#while ishora:
 #   buyurtma = input('Buyurtma nomini kiriting \n>>')    
#    takrorlash = input("Yana biror narsa buyurtma qilishni xoxlaysizmi (ha/yo'q)")
#    buyurtmalar.append(buyurtma)
#    if takrorlash == "yo'q":
#        ishora = False
#print("Sizning buyurtmalaringiz")
#for zakaz in buyurtmalar:
 #   print(zakaz)


e_bozor = {}
#print("Keling online bozor yaratamiz")

#while True:
    #mahsulot = input("Mahsulot nomini tanlang (jarayonni to'xtatish uchun 'stop' deb yozing): ")
    #if mahsulot == 'stop':
    #  break
   # narh = input(f"{mahsulot}ga narh belgilang: ")
  #  narh = int(narh)
 #   e_bozor[mahsulot] = narh
    
       
        
#print("Bozordagi mahsulotlar ro'yxati")
#for key, value in e_bozor.items():
 #   print(f"{key.title()} : {value}")




cars = []
for n in range(10):
    new_car = {'model': "molibu",
               'rang':'oq',
               'km':0,
               'yil':2023,
               'karobka': 'avtomat'}
    cars.append(new_car)
for car in cars[:3]:
   car['rang'] = 'qizil'
for car in cars[6:]:
    car['karobka'] = 'mexanik'
if car['karobka']== 'avtomat': 
    car['km'] = 10000
print(    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    