from abc import ABC,abstractmethod

class Servicable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

    @abstractmethod 
    def does_not_needs_service(self):
        pass