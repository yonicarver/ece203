class bug:
    def __init__(self,position):
        self.position = position
        self.direction = 'right'

    def turn(self):
        if self.direction == 'right':
            self.direction == 'left'
        elif self.direction == 'left':
            self.direction == 'right'

    def move(self):
        if self.direction == 'right':
            self.position += 1
        elif self.direction == 'left':
            self.position -= 1
    
    def pos(self):
        return self.position
    
    def dir(self):
        return self.direction

ant = bug(10)
ant.move()
ant.turn()
ant.move()
ant.move()
print ant.pos()
print ant.dir()
