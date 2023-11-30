from datetime import datetime
from battery import Battery

class Spindler_Battery(Battery):
    def _init_(self,last_service_date,current_date):
        super.__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_needs_service(self):
        service_threshold_rate = self.last_service_date.replace(year=self.last_service_date + 2)
        current_date = datetime.today()

        if service_threshold_rate < current_date :
            return True
        else:
            return False