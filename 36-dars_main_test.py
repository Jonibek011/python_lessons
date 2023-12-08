import unittest
from main import*
# from main import get_info
# from main import get_fullname
# class MainTest(unittest.TestCase):
#     def test_fullname(self):
#         toliq_ism = get_fullname('jonibek', 'orifjonov')
#         self.assertEqual(toliq_ism, 'Jonibek Orifjonov')
 
# class MainTest1(unittest.TestCase):
#     def test_ism_sharf(self):
#         tism = ism_sharf('orifjonov', 'jonibek', 'baxromjonovich')
#         self.assertEqual(tism,"Orifjonov Jonibek Baxromjonovich")

# class Get_info(unittest.TestCase):
#     def test_info(self):
#         info = get_info('jonibek', 'orifjonov', 1996)
#         self.assertEqual(info, "Jonibek Orifjonov, 1996 -yilda tug'ilgan")

# class Katta_son(unittest.TestCase):
#     def test_kattason(self):
#         data = katta_son(1,2,3)
#         self.assertEqual(data, '3 katta')

# class Katta_harf(unittest.TestCase):
#     def test_bosh_harf(self):
#         data = Bosh_harf(nomlar)
#         self.assertEqual(data, ['Ali', 'Vali', 'Jalil', 'Ahmad'])
# unittest.main()

# class Juft_sonlar(unittest.TestCase):
#     def test_juft_son(self):
#         son1 = juft_sonlar(10)
#         self.assertEqual(son1, [2, 4, 6, 8])


class Fibonacci(unittest.TestCase):
    def test_fnacci(self):
        fsoni = Fibonacci_soni(10)
        self.assertTrue(fsoni, True)
unittest.main()










