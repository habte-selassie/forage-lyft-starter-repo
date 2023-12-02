from engine.tires.tire import Tire

class OctoPrime_Tires(Tire):
    @staticmethod
    def tire_needs_service(test_wear_sensors):
        needs_to_provide_service = False
        test_wear_sensors = [0.1,0.9,0.8,0.9]

        sum_value_of_test_wear_sensors = sum(test_wear_sensors)
        
        if sum_value_of_test_wear_sensors >= 3:
            needs_to_provide_service = True
           
        return needs_to_provide_service
    
octoprime_tire_wear = [0.2, 0.6, 0.8, 1.0]
 

if OctoPrime_Tires.tire_needs_service(octoprime_tire_wear):
     print ("octoprime tire should give service")
else:
    print ("octoprime tire should not give service")