
class Car:
    def __init__(self, efficiency, init_gas):
        self.efficiency = float(efficiency)
        self.init_gas = 0
        self.add_gas = 0
        
    def add_gas(self, amount_gas):
        self.init_gas += amount_gas

    def drive(self, distance):
        """ simulates driving car, reduces fuel level in tank """
        self.distance = distance
        if self.init_gas*self.efficiency >= distance:
            print 'enough gas'
        else:
            print 'not enough gas'
        #max_distance = self.efficiency * initial_gas
        #if max_distance > self.distance:
        #    self.drive = 'True'
        #else:
        #    self.drive = 'False'
        #return self.drive

    def get_gas_level(self):
        #self.getgaslevel = self.distance/self.efficiency
        self.init_gas -= self.distance/self.efficiency
        
    


h = Car(0,50)
h.add_gas(2)
h.drive(75)
h.get_gas_level()
