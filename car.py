from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
from my_interface_module import Servicable

class Car(Engine,Battery,Servicable):
    def __init__(self, engine,battery):
        self.engine = engine
        self.battery = battery
    
    def needs_service(self):
        return self.battery.battery_needs_service() and self.engine.engine_needs_service()

    def doesnot_needs_service(self):
        return not (self.battery.battery_needs_service() and self.engine.engine_needs_service())
    
    def battery_needs_service(self):
        return self.battery.battery_needs_service()
    
    def engine_needs_service(self):
        return self.engine.engine_needs_service()
    
    def servicable(self):
        return self.battery.battery_needs_service() or self.engine.engine_needs_service()


