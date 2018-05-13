from GeneticAlgo.Creature import Creature
from Vectors import Vector2

class Generation:
    pathMultiplier = 2
    fitnessMultiplier = 100
    startingPoint=Vector2()
    def __init__(self,gameObject,dna,targetObject):
        self.creature = Creature(gameObject,dna)
        self.creature.gameObject.position = Generation.startingPoint
        self.target = targetObject
        self.nextPoint = self.creature.gameObject.position;
        self.pathIndex=0
        self.finished = False
        self.initialised = True
        
    
    def loop(self):
        if(self.initialised and not self.finished):
            if(self.pathIndex == len(self.creature.dna.PositionGenes) or Vector2.Distance(self.creature.gameObject.position, self.target.position) < 0.5):
                self.finished = True
                
            if(self.creature.gameObject.position == self.nextPoint):
                self.nextPoint = self.creature.gameObject.position + self.creature.dna.PositionGenes[self.pathIndex]*Generation.pathMultiplier
                self.pathIndex+=1

            else:
                self.creature.gameObject.position = Vector2.MoveToward(self.creature.gameObject.position, self.nextPoint, self.creature.gameObject.speed)
    
    
    def draw(self,gameDisplay):
        self.creature.gameObject.draw(gameDisplay)
    
        
    def getFitness(self):
        dist = Vector2.Distance(self.creature.gameObject.position, self.target.position)
        if(dist==0):
            dist=0.0001
            
        self.creature.fitness = (Generation.fitnessMultiplier/dist)
        return self.creature.fitness