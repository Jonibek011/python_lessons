import random
def sontop(n):
    son =random.randint(1,n)
    print(f"Keling son topish o'yinini o'ynaymiz, men 1 dan {n} gacha bo'lgan bir son o'yladim topib ko'ringchi: ")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input('>>>'))
        if taxmin >son:
            print(f"Xato men o'ylagan son {taxmin} dan kichikroq: ")
        elif taxmin < son:
            print(f"Xato men o'ylagan son {taxmin} dan kattaroq: ")           
        else:
            break
    print(f"To'g'ri, siz javobni {taxminlar} urinishda topdingiz!!! ")    