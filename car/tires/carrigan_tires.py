from .tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear=[0,0,0,0]) -> None:
        super().__init__(tire_wear)

    def needs_service(self):
        return any(wear > 0.9 for wear in self.tire_wear) 