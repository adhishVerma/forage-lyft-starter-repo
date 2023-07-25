from car.car import Car

from car.engine.willoughby_engine import WilloughbyEngine
from car.battery.spindler_battery import SpindlerBattery


class Glissade(Car):
    def __init__(self, last_service_date, current_mileage ,last_service_mileage):
        super().__init__(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date))
    
