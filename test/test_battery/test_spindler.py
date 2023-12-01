import unittest
from datetime import datetime
from engine.batterys.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):

      def test_battery_should_give_service(self):
         current_date =  datetime.fromisoformat("2023-10-10")
         last_service_date = datetime.fromisoformat("2021-10-10")
         battery = SpindlerBattery(current_date,last_service_date)
         self.assertTrue(battery.needs_service())

      def test_battery_should_not_give_service(self):
         current_date =  datetime.fromisoformat("2023-10-10")
         last_service_date = datetime.fromisoformat("2022-10-10")
         battery = SpindlerBattery(current_date,last_service_date)
         self.assertFalse(battery.needs_service())                   


if __name__ == '__main__':
    unittest.main()
