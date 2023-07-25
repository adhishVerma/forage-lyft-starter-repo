from car.car import Car

from car.engine.capulet_engine import CapuletEngine
from car.battery.nubbin_battery import NubbinBattery


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage ,last_service_mileage):
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date))
    
