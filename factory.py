from car import Car
from engine.batterys.nubbin_battery import NubbinBattery
from engine.batterys.spindler_battery import SpindlerBattery
from engine.engine0.capulet_engine import CapuletEngine
from engine.engine0.sternman_engine import SternmanEngine
from engine.engine0.willoughby_engine import WilloughbyEngine

class CarFactory:
     @staticmethod
     def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage): 
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine,battery)
        return car
    
     @staticmethod
     def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage): 
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine,battery)
        return car

     @staticmethod
     def create_palindrome(current_date, last_service_date,warning_light_on): 
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine,battery)
        return car

     @staticmethod
     def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage): 
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine,battery)
        return car


     @staticmethod
     def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage): 
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine,battery)
        return car        
    
   