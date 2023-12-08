
# def get_fullname(ism, familiya):
 #   """Ism va familiya qabul qilib fullname qaytaruvchi funksiya"""
#     return f"{ism} {familiya}".title()

# def ism_sharf(familiya, ism, sharf):
    #"""Ism sharif qabul qilib fullname qabul qiluvchi funksiya"""
#     return f"{familiya} {ism} {sharf}".title()

# def get_info(ism, familiya, tyil):
   # """Ism, familiya, tug'ilgan yil qabul qilib to'liq ma'lumot qaytaruvchi funksiya"""
#     return f"{ism.title()} {familiya.title()}, {tyil} -yilda tug'ilgan"
# print(get_info('jonibek','orifjonov', 1996))

# def katta_son(x,y,z):
    #"""Kiritilgan sonlardan kattasini qaytaruvchi funksiya"""
#     if x > y and x > z:
#         return f"{x} katta"
#     elif y>x and y>z:
#         return f"{y} katta"
#     else:
#         return f"{z} katta"
# print(katta_son(1,2,3))    


# def Bosh_harf(ismlar):
    #"""Ro'yxat qabul qilib ma'lumotlarni bosh harflarga o'zgartiruvchi funksiya"""
#     names = []
   
#     for ism in ismlar:
#         ism = ism.title()
#         names.append(ism)
#     return names
        
# nomlar = ['ali', 'vali', 'jalil', 'ahmad']  
    
# def juft_sonlar(n):
    #"""Berilgan sonlardan juft sonlarni qaytaruvchi funksiya"""
#     sonlar = []
#     for son in range(n):
#         if son ==0:
#             continue
#         elif son % 2 ==0:
#             sonlar.append(son)
#         else:
#             continue
#     return sonlar
        
#print(juft_sonlar(10))



def Fibonacci_soni(n):
    """Berilgan sonlarda fibanacci sonlari bor yo'qligini qaytaruvchi funksiya"""
    sonlar = []
    for son in range(n):
        if son == 0:
            continue
        elif son ==((son-1)+(son-2)):
            sonlar.append(son)
            
        else:
            continue
    if sonlar:
        return True

    
    
    
    