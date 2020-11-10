from math import pi

class SodaCan:
    """ output: surface area and volume """
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
    def getSurfaceArea(self):
        """ find surface area of soda can """
        surfacearea = float((2*pi*self.radius*self.height)+(2*pi*self.radius**2))
        print surfacearea
        
    def getVolume(self):
        """ find volume of soda can """
        volume = float((pi*(self.radius**2)*self.height))
        print volume

test1 = SodaCan(2,4)

test1.getSurfaceArea()
test1.getVolume()
