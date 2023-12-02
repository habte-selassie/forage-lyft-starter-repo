from car import Car
from engine.batterys.nubbin_battery import NubbinBattery
from engine.batterys.spindler_battery import SpindlerBattery
from engine.engine0.capulet_engine import CapuletEngine
from engine.engine0.sternman_engine import SternmanEngine
from engine.engine0.willoughby_engine import WilloughbyEngine
from engine.tires.carrigan_tires import CarriganTires
from engine.tires.octoprime_tires import OctoPrimeTires

class CarFactory:
     @staticmethod
     def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear_sensors): 
          engine = CapuletEngine(last_service_mileage, current_mileage)
          battery = SpindlerBattery(last_service_date, current_date)
          tire_wear_sensors = [0.1,0.2,0.3,0.6]

          tire = None

        
          if any (value >= 0.9 for value in tire_wear_sensors):
              tire = CarriganTires(tire_wear_sensors)
          else :
              print("Values in Tire wear sensor are less than 0.9 so no Carrigan Tire be Uses")  

          if sum(tire_wear_sensors) >= 3:
              tire1 = OctoPrimeTires(tire_wear_sensors)
          else:
              print("sum of tire_wear_sensors are less than three hence no octoprime tires")          
               

          car = Car(engine,battery,tire,tire1)
          return car
    
     @staticmethod
     def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear_sensors): 
          engine = WilloughbyEngine(last_service_mileage, current_mileage)
          battery = SpindlerBattery(last_service_date, current_date)
          tire_wear_sensors = [0.1,0.2,0.3,0.6]

          tire = None

        
          if any (value >= 0.9 for value in tire_wear_sensors):
              tire = CarriganTires(tire_wear_sensors)
          else :
              print("Values in Tire wear sensor are less than 0.9 so no Carrigan Tire be Uses")  

          if sum(tire_wear_sensors) >= 3:
              tire1 = OctoPrimeTires(tire_wear_sensors)
          else:
              print("sum of tire_wear_sensors are less than three hence no octoprime tires")          
               

          car = Car(engine,battery,tire,tire1)
          return car 
       
     @staticmethod
     def create_palindrome(current_date, last_service_date,warning_light_on,tire_wear_sensors): 
          engine = SternmanEngine(warning_light_on)
          battery = SpindlerBattery(last_service_date, current_date)
          tire_wear_sensors = [0.1,0.2,0.3,0.6]

          tire = None

        
          if any (value >= 0.9 for value in tire_wear_sensors):
              tire = CarriganTires(tire_wear_sensors)
          else :
              print("Values in Tire wear sensor are less than 0.9 so no Carrigan Tire be Uses")  

          if sum(tire_wear_sensors) >= 3:
              tire1 = OctoPrimeTires(tire_wear_sensors)
          else:
              print("sum of tire_wear_sensors are less than three hence no octoprime tires")          
               

          car = Car(engine,battery,tire,tire1)
          return car
       

     @staticmethod
     def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear_sensors): 
          engine = WilloughbyEngine(last_service_mileage, current_mileage)
          battery = NubbinBattery(last_service_date, current_date)
          tire_wear_sensors = [0.1,0.2,0.3,0.6]

          tire = None

        
          if any (value >= 0.9 for value in tire_wear_sensors):
              tire = CarriganTires(tire_wear_sensors)
          else :
              print("Values in Tire wear sensor are less than 0.9 so no Carrigan Tire be Uses")  

          if sum(tire_wear_sensors) >= 3:
              tire1 = OctoPrimeTires(tire_wear_sensors)
          else:
              print("sum of tire_wear_sensors are less than three hence no octoprime tires")          
               

          car = Car(engine,battery,tire,tire1)
          return car
        


     @staticmethod
     def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage,tire_wear_sensors): 
          engine = CapuletEngine(last_service_mileage, current_mileage)
          battery = NubbinBattery(last_service_date, current_date)
          tire_wear_sensors = [0.1,0.2,0.3,0.6]

          tire = None

        
          if any (value >= 0.9 for value in tire_wear_sensors):
              tire = CarriganTires(tire_wear_sensors)
          else :
              print("Values in Tire wear sensor are less than 0.9 so no Carrigan Tire be Uses")  

          if sum(tire_wear_sensors) >= 3:
              tire1 = OctoPrimeTires(tire_wear_sensors)
          else:
              print("sum of tire_wear_sensors are less than three hence no octoprime tires")          
               

          car = Car(engine,battery,tire,tire1)
          return car
                
    
   