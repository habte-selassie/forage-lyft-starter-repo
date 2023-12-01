import unittest
from datetime import datetime
from utils import add_years_to_date

from engine.batterys.nubbin_battery import NubbinBattery
from engine.batterys.spindler_battery import SpindlerBattery
from engine.engine0.capulet_engine import CapuletEngine
from engine.engine0.sternman_engine import SternmanEngine
from engine.engine0.willoughby_engine import WilloughbyEngine


class CapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
    
        if current_mileage - last_service_mileage > 30000:

         self.assertTrue(engine.needs_service())


    def test_engine_should_not_be_serviced(self):
         current_mileage = 30000
         last_service_mileage = 0

         engine = CapuletEngine(current_mileage, last_service_mileage)


         if current_mileage - last_service_mileage <= 30000:

          self.assertFalse(engine.needs_service())


class WilloughbyEngine(unittest.TestCase):
      def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
    
        if current_mileage - last_service_mileage > 60000:

         self.assertTrue(engine.needs_service())


      def test_engine_should_not_be_serviced(self):
          current_mileage = 60000
          last_service_mileage = 0

          engine = WilloughbyEngine(current_mileage, last_service_mileage)


          if current_mileage - last_service_mileage <= 60000:

           self.assertFalse(engine.needs_service())   


class SternmanEngine(unittest.TestCase):
      def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
    
        if warning_light_is_on:
         self.assertTrue(engine.needs_service())


      def test_engine_should_not_be_serviced(self):
          warning_light_is_on = False

          engine = SternmanEngine(warning_light_is_on)

          if warning_light_is_on:
           self.assertFalse(engine.needs_service()) 


class NubbinBattery(unittest.TestCase):

      def battery_should_give_service(self):
         current_date_time =datetime.now()
         current_date = current_date_time.date() 
         date_nubin_battery_needs_to_serve = add_years_to_date(self.last_service_date,4)
         
        
         if date_nubin_battery_needs_to_serve < current_date :
            self.assertTrue(needs_service())

      def battery_should_not_give_service(self):
         current_date_time =datetime.now()
         current_date = current_date_time.date() 
         date_nubin_battery_needs_to_serve = add_years_to_date(self.last_service_date,4)

         if date_nubin_battery_needs_to_serve > current_date :
            self.assertFalse(needs_service())         


class SpindlerBattery(unittest.TestCase):

      def battery_should_give_service(self):
         current_date_time =datetime.now()
         current_date = current_date_time.date() 
         date_nubin_battery_needs_to_serve = add_years_to_date(self.last_service_date,2)

         if date_nubin_battery_needs_to_serve < current_date :
            self.assertTrue(needs_service())

      def battery_should_not_give_service(self):
         current_date_time =datetime.now()
         current_date = current_date_time.date() 
         date_nubin_battery_needs_to_serve = add_years_to_date(self.last_service_date,2)

         if date_nubin_battery_needs_to_serve > current_date :
            self.assertFalse(needs_service())                   


if __name__ == '__main__':
    unittest.main()
