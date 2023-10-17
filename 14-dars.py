#14-dars Lug'atlar bilan ishlash
#car_0 = {"model":"Bugatti", "rang":'qora'}
#print(car_0["model"])
#print(car_0["rang"])
#dictionary = {"apple":"olma", "cow":"sigir", "car":"mashina", "ruster":"xo'roz"}
#print(dictionary["apple"])

#mevalar = {"olma":10000, "o'rik":12000, 'shaftoli':15000}
#print(f"olmaning narxi {mevalar['olma']} so'm")


#talaba_0 = {"ism":"jalilov Dilshod", "yosh":20, "t_yil":2003}
#print(f"Talabaning ismi {talaba_0['ism'].title()}, \
#yoshi {talaba_0['yosh']} da, \
#{talaba_0['t_yil']} - yilda tug'ilgan")
#talaba_0['kurs'] = 4
#talaba_0['fakultet'] = "informatika"
#print(talaba_0)
#talaba_0['ism'] = "Abdulloh"
#print(talaba_0)


talaba_1 = {}
talaba_1['ism'] = 'sherzod olimov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 23
#print(talaba_1)
#print(f"Talabaning ismi {talaba_1['ism'].title()}, \
#{talaba_1['kurs']} - kursda o'qiydi, yoshi {talaba_1['yosh']} da")
talaba_1['kurs'] = 4
#print(f"Talabaning ismi {talaba_1['ism'].title()}, \
#{talaba_1['kurs']} - kursda o'qiydi, yoshi {talaba_1['yosh']} da")


#telefonlar = {
#    'Ali':'Iphone x',
 #   'Vali':'Galaxi S9'
 #  }
#print(telefonlar)


# get metodi

sohalar = {"sardor":'kardiolog', "o'tkir":'nevropatolog','islom':'urolog'}
mutaxassisliklar = sohalar.get("sattor", 'Bizda bunday ismli mutaxassis mavjud emas')
print(mutaxassisliklar)
