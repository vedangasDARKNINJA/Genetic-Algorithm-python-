
class Creature:
    def __init__(self,gameObject,dna,speed=None):
        self.gameObject = gameObject
        self.dna = dna
        self.fitness = 0.0
        
        if(speed!= None):
            self.gameObject.speed=speed
        else:
            self.gameObject.speed=50