

import unittest
from Cars import Car

class CarTest(unittest.TestCase):
    def setUp(self):
        make = 'GM'
        model = 'Molibu'
        yil = 2020
        rang = 'qora'
        self.narh = 40000
        self.km = 10000
        self.avto1 = Car(make, model, yil, rang)
        self.avto2 = Car(make, model,  yil, rang, narh = self.narh)
    
    def test_create(self):
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.yil)
        self.assertIsNotNone(self.avto1.rang)
        self.assertIsNone(self.avto1.narh)
        self.assertIsNotNone(self.avto2.narh)
        
        self.assertEqual(self.avto1.get_km(), 0)
        self.assertEqual(self.narh, self.avto2.narh)
    def test_set_narh(self):
        self.avto1.set_narh(30000)
        self.assertEqual(self.avto1.narh, 30000)
    
    def test_add_km(self):
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        test_km = -5000
        try:
          self.avto1.add_km(test_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    

unittest.main()

