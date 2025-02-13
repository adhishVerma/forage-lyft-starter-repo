from car.car import Car

from car.engine.capulet_engine import CapuletEngine
from car.battery.nubbin_battery import NubbinBattery
from car.tires.carrigan_tires import CarriganTires



class Thovex(Car):
    def __init__(self, last_service_date, current_mileage ,last_service_mileage,tire_wear=[0,0,0,0]):
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date), CarriganTires(tire_wear))
    
