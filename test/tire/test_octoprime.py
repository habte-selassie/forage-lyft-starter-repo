import unittest

class TestCarrigan(unittest.TestCase):
    def test_carrigan_tire_should_service(self):
        tire_wear_value = [0.1,0.2,0.3,1.0]
        tire_wear_value_sum = sum(tire_wear_value)
        self.assertGreaterEqual(tire_wear_value_sum,3)

    def test_carrigan_tire_should_not_service(self):
        tire_wear_value = [0.1,0.2,0.3,1.0]
        tire_wear_value_sum = sum(tire_wear_value)
        self.assertGreaterEqual(tire_wear_value_sum,2.99)    
        