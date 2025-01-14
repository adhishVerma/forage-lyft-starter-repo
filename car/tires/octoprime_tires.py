from .tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wear) -> None:
        super().__init__(tire_wear)
    
    def needs_service(self):
        return sum(self.tire_wear) > 3