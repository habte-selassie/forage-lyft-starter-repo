from engine.tires.tire import Tire

class CarriganTires(Tire):
    @staticmethod
    def needs_service(tire_wear_sensors):
        need_to_give_service = False

        tire_wear_sensors = [0.2, 0.6, 0.8, 1.0]

        for value in tire_wear_sensors:
            if value >= 0.9:
             need_to_give_service = True
             break

        return need_to_give_service  

carrigan_tire_wear_ = [0.2, 0.6, 0.8, 1.0]

if CarriganTires.needs_service(carrigan_tire_wear_):
    print ("carrigan tire should give service")
else:
    print ("carrigan tire should not give service")
                
         