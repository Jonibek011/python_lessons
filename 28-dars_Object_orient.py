 # 12.11.2023
# Objekt va Orientlar


class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.name = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.familiya
    def get_tyil(self):
        return self.tyil
    def get_age(self, yil):
       
        return f"{self.name} {yil - self.tyil} yoshda "
    
    def tanishtir(self):
      return f"Mening ismim {self.name} {self.familiya} tug'ilgan yilim {self.tyil}"


talaba1 = Talaba("Olim", "olimov", 2001)
talaba2 = Talaba("Jonibek", "Orifjonov", 1995)
talaba3 = Talaba("Anvar", "Narzullayev", 1985)

# AMALIY QISM

class User:
    def __init__(self, first_name, last_name, user_name, email):
        self.name = first_name
        self.lname = last_name
        self.uname = user_name
        self.mail = email
    def get_name(self):
        return self.name
    def get_lname(self):
        return self.lname
    def get_mail(self):
        return self.mail
    def get_info(self):
        return f"Foydalanuvchining ismi {self.name} {self.lname}, email addresi: {self.mail}"
user = User("Jonibek", "Orifjonv", 'John', "jonibektank@gmail.com")


    
   
    
    
    



        
