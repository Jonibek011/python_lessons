

class Car:
    def __init__(self, make, model, rang, yil, km = 0, narh = None):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil =yil
        self.narh = narh
        self.__km = km
        
    def add_km(self, x):
        if x > 0: 
           self.__km += x
        else:
            raise ValueError("km manfiy co'lishi mumkin emas")
    
    def get_info(self):
        info = f"{self.rang.title()} {self.model}, {self.make.upper()} da ishlab chiqarilgan. {self.__km} km yurgan. "
        if self.narh:
            info += f"Narhi: {self.narh}"
        return info
    
    def set_narh(self, narh):
        self.narh = narh
        
    def get_km(self):
        return self.__km


















