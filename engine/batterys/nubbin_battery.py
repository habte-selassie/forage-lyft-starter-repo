from datetime import datetime
from battery import Battery

class Nubbin_Battery(Battery):
    def _init_(self,last_service_date,current_date):
         super. _init_(last_service_date)
         self.last_service_date = last_service_date
         self.current_date = current_date
    
    def baterry_needs_service(self):
         service_threshold_date = self.last_service_date.replace(year = self.last_service_date + 4)
         current_date = datetime.today.date()
         if service_threshold_date < current_date :
               return True
         else :
               return  False           

