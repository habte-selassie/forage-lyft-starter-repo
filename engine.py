from abc import ABC,abstractmethod

class Engine(ABC):
    def __init__(self,last_service_mileage, currnet_mileage,warning_indicator_on = False) -> None:
        super().__init__(last_service_mileage)
        self.last_service_mileage = last_service_mileage
        self.current_mileage = currnet_mileage
        self.warning_indicator_on = warning_indicator_on

    @abstractmethod
    def engine_needs_service(self):
        pass    