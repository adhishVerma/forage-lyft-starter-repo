from datetime import datetime

from .battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_Service_date):
        super().__init__(last_Service_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date()