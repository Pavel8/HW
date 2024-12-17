import unittest

class Cisla
    def __init__(self):
        self.set_cisel = set(10,20,30)
    
    def soucet(self):
            return sum(self.set_cisel)
    
    def ar_mean(self):
            if len(self.set_cisel) > 0:
                return sum(self.set_cisel) / len(self.set_cisel)
            else:
                return None
            
    def maximum(self):
        if self.set_cisel:
            return max(self.set_cisel)
        else:
            return None
        
    def minimum(self):
        if self.set_cisel:
            return min(self.set_cisel)
        else:
            return None


class TestCisla(unittest.TestCase):
    
    def setUp(self):
        self.cisla_obj = Cisla()
    
    def test_soucet(self):
        self.assertEqual(self.cisla_obj.soucet(), 60) 

    def test_ar_mean(self):
        self.assertEqual(self.cisla_obj.ar_mean(), 20.0) 
    
    def test_maximum(self):
        self.assertEqual(self.cisla_obj.maximum(), 30)  

    def test_minimum(self):
        self.assertEqual(self.cisla_obj.minimum(), 10)
    


    def test_empty_set(self):
        # test setu kdyz je prazdny
        empty_cisla = Cisla()
        empty_cisla.set_cisel = set()
        
        self.assertEqual(empty_cisla.soucet(), 0) 
        self.assertIsNone(empty_cisla.ar_mean())  
        self.assertIsNone(empty_cisla.maximum())  