from GeneticAlgo.Generation import Generation
from GeneticAlgo.DNA import DNA
from car import Car
from Vectors import Vector2
import numpy as np



class Population:
    Once = False
    def __init__(self,gameObject,startingPoint,targetObject):
        self.populationSize = 200
        self.genomeLength=200
        self.populationCutOff =0.15
        self.generationCount = 1
        self.go = gameObject
        self.target = targetObject
        self.startingPoint = startingPoint
        
        self.ErrorVec=Vector2()
        self.LastFittest = Generation(Car(gameObject),DNA(self.genomeLength),targetObject)
        
        self.population = []
        self.survivors = []
        for i in range(self.populationSize):
            gen = Generation(Car(gameObject),DNA(self.genomeLength),targetObject)
            gen.creature.gameObject.position = startingPoint
            self.population.append(gen)
        
        
          
            
    def simulate(self,gameDisplay):
#         self.ErrorVec = (self.target.position-self.GetFittestPopulation().creature.gameObject.position)
#         if(self.ErrorVec.magnitude()>10):
#             Generation.pathMultiplier = self.ErrorVec.magnitude()*0.05
#         else:
#             Generation.pathMultiplier = 2
        
        if( not self.HasActive()):
            Population.Once = False
            self.NextGeneration()
                   
        if(len(self.population) > 0):
            for i in range(self.populationSize):
                self.population[i].loop()
                self.population[i].draw(gameDisplay) 
            
        
               
    def HasActive(self):
        for i in range(len(self.population)):
            if(not self.population[i].finished):
                return True
            return False
        
    
    def GetFittest(self):
        maxFit = 0.0
        index = 0
        for i in range(len(self.population)):
            if(self.population[i].getFitness() > maxFit):
                maxFit = self.population[i].creature.fitness
                index = i

        
        
        fittest = self.population[index]
        del self.population[index]
        return fittest
    
    def GetFittestPopulation(self):
        maxFit = 0.0
        index = 0
        for i in range(len(self.population)):
            if(self.population[i].getFitness() > maxFit):
                maxFit = self.population[i].creature.fitness
                index = i

        
        
        fittest = self.population[index]
        return fittest
     
    def NextGeneration(self):
        self.generationCount+=1
        print(self.generationCount)
        survivorsCutoff = round(self.populationSize*self.populationCutOff)
        for i in range(survivorsCutoff):
            self.survivors.append(self.GetFittest())
            if(i<10):
                if( i == 0):
                    self.LastFittest = self.survivors[0]
                    self.ErrorVec = self.target.position - self.survivors[0].creature.gameObject.position
                    
                    print("Target Position: ",self.target.position)
                    print("survivor[0] Position:", self.survivors[0].creature.gameObject.position)
                    print("X_Error : ", self.ErrorVec.x)
                    print("Y_Error : ", self.ErrorVec.y)
                    print("Error_mag: ",self.ErrorVec.magnitude())
                    print("Path Multiplier: ",Generation.pathMultiplier)
                print("survivor[",i," Fitness: ",self.survivors[i].creature.fitness)
        
        self.population.clear()
        
        while(len(self.population) < self.populationSize):
            for i in range(len(self.survivors)):
                gen = Generation(Car(self.go),DNA(self.genomeLength,self.survivors[np.random.randint(0,10)].creature.dna,self.survivors[np.random.randint(0,10)].creature.dna),self.target)
                gen.creature.gameObject.position = self.startingPoint
                self.population.append(gen)
                if len(self.population) >= self.populationSize:
                    break
                    
        self.survivors.clear()      