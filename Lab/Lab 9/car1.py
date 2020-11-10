class Car:
    def __init__(self, efficiency):
        self.efficiency = float(efficiency)
        self.gas_level = 0
                    
    def add_gas(self, amount_gas):
        self.gas_level += amount_gas
                     
    def drive(self, distance):
        """ simulates driving car, reduces fuel level in tank """
                                           
        max_distance = self.gas_level * self.efficiency
                                       
        if max_distance > distance:
            self.gas_level -= float(distance)/self.efficiency
            return True
        else:
            self.gas_level = 0
            return False
                                                         
    def get_gas_level(self):
        return self.gas_level

h = Car(0,50)
h.add_gas(2)
if h.drive(75):
    print h.get_gas_level()
else:
    print 'not enough gas'
    
