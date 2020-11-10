class Car:
    def __init__(self,gal,mpg):
        self.mpg = float(mpg)
        self.gal = float(gal)
        
    def drive(self,miles):
        self.miles = miles
        
        if self.mpg*self.gal >= miles:
            print 'Enough gas'
        else:
            print 'Not enough gas'
            
    def addGas(self,gasin):
        self.gal += gasin
    
    def getGasLevel(self):
        self.gal -= self.miles/self.mpg
        print '%s gallons remaining' % self.gal

hybrid = Car(0,50)
hybrid.addGas(2)
hybrid.drive(75)
hybrid.getGasLevel()
