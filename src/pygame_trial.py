import pygame
from GeneticAlgo.Population import Population 
from car import car4
from Vectors import Vector2
import GeneticAlgo

dis_w = 800
dis_h = 600
def gameInit(w,h,title='PyGame'):
    pygame.init()
    
    #GAME WINDOW INIT
    gameDisplay = pygame.display.set_mode((w, h))
    pygame.display.set_caption(title)
    return gameDisplay



startingPoint = Vector2(dis_w*0.5,dis_h*0.5)
gameDisplay = gameInit(dis_w, dis_h, "Genetic Algo")
clock = pygame.time.Clock()

#colors
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)


car4.setLocation(Vector2((startingPoint.x-125),(startingPoint.y-150)))
GeneticAlgo.Generation.Generation.startingPoint = startingPoint
p = Population('car1.png',startingPoint,car4)

#CRASH CHECK
crashed = False
while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        car4.getKey(event)
        
    
    gameDisplay.fill(White)         
    car4.move()
    car4.draw(gameDisplay)
    p.simulate(gameDisplay)
    
    pygame.display.update()
    
    clock.tick(60)
    
pygame.quit()
quit()