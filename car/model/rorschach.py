from car.car import Car

from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery

class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage ,last_service_mileage):
        super().__init__(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date))
    