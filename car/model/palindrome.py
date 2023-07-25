from car.car import Car

from car.engine.sternman_engine import SternmanEngine
from car.battery.spindler_battery import SpindlerBattery
from car.tires.carrigan_tires import CarriganTires


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on,tire_wear=[0,0,0,0]):
        super().__init__(SternmanEngine(warning_light_is_on), SpindlerBattery(last_service_date), CarriganTires(tire_wear))
    
