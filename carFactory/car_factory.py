from car.model import calliope, glissade, palindrome, rorschach, thovex

class CarFactory:

    def create_calliope(self, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return calliope.Calliope(last_service_date, current_mileage, last_service_mileage, tire_wear)
    
    def create_glissade(self, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return glissade.Glissade(last_service_date, current_mileage, last_service_mileage, tire_wear)

    def create_palindrome(self, last_service_date, warning_light_is_on, tire_wear):
        return palindrome.Palindrome(last_service_date, warning_light_is_on, tire_wear)

    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage, tire_wear):
        return rorschach.Rorschach(last_service_date, current_mileage, last_service_mileage, tire_wear)
    
    def create_thovex(self,last_service_date, current_mileage, last_service_mileage, tire_wear):
        return thovex.Thovex(last_service_date, current_mileage, last_service_mileage, tire_wear)