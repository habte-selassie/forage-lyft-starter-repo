import unittest
from datetime import datetime
from engine.batterys.nubbin_battery import NubbinBattery


class NubbinBattery(unittest.TestCase):

      def test_battery_should_give_service(self):
         current_date = datetime.fromisoformat("2023-12-29")
         last_service_date = datetime.fromisoformat("2018-01-19")
         battery = NubbinBattery(current_date,last_service_date)
         self.assertTrue(battery.needs_service())

      def test_battery_should_not_give_service(self):
         current_date = datetime.fromisoformat("2023-12-29")
         last_service_date = datetime.fromisoformat("2020-01-19")
         battery = NubbinBattery(current_date,last_service_date)
         self.assertFalse(battery.needs_service())         


if __name__ == '__main__':
    unittest.main()
