from engine.tires.tire import Tire

class Carrigan_Tires(Tire):
    @staticmethod
    def should_service_tires(tire_wear_sensors):
        need_to_give_service = False

        tire_wear_sensors = [0.2, 0.6, 0.8, 1.0]

        for value in tire_wear_sensors:
            if value >= 0.9:
             need_to_give_service = True
             break

        return need_to_give_service  

carrigan_tire_wear_ = [0.2, 0.6, 0.8, 1.0]

if Carrigan_Tires.should_service_tires(carrigan_tire_wear_):
    print ("carrigan tire should give service")
else:
    print ("carrigan tire should not give service")
                
         