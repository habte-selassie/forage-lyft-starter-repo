import unittest

class TestCarrigan(unittest.TestCase):
    def test_carrigan_tire_should_service(self):
        tire_wear_value = [0.1,0.2,0.3,1.0]
        tire_wear_value[0] = [0.1]
        tire_wear_value[1] = [0.2]
        tire_wear_value[2] = [0.3]
        tire_wear_value[3] = [1.0]

        self.assertGreaterEqual(tire_wear_value[0],0.9)
        self.assertGreaterEqual(tire_wear_value[1],0.9)
        self.assertGreaterEqual(tire_wear_value[2],0.9)
        self.assertGreaterEqual(tire_wear_value[3],0.9)

    def test_carrigan_tire_should_not_service(self):
        tire_wear_value = [0.1,0.2,0.3,1.0]
        tire_wear_value[0] = [0.1]
        tire_wear_value[1] = [0.2]
        tire_wear_value[2] = [0.3]
        tire_wear_value[3] = [1.0]

        self.assertLess(tire_wear_value[0],0.9)
        self.assertLess(tire_wear_value[1],0.9)
        self.assertLess(tire_wear_value[2],0.9)
        self.assertLess(tire_wear_value[3],0.9)