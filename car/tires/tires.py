from abc import ABC, abstractmethod

class Tires(ABC):

    def __init__(self, tire_wear) -> None:
        self.tire_wear = tire_wear
    
    @abstractmethod
    def needs_service(self):
        pass