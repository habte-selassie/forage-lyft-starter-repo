from datetime import datetime
from engine.batterys.battery import Battery
from utils import add_years_to_date
class SpindlerBattery(Battery):
    def _init_(self,last_service_date,current_date):
        super.__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_needs_to_serve = add_years_to_date(self.last_service_date,3)
        current_date_time = datetime.now()
        current_date = current_date_time.date()
        if date_which_battery_needs_to_serve < current_date :
            return True
        else:
            return False