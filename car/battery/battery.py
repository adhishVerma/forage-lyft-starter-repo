from abc import abstractmethod, ABC

class Battery(ABC):
    def __init__(self, last_service_date) -> None:
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass