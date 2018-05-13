import pygame
from Vectors import Vector2
import math

class Car(): 
    moveStep = 0.01
        
    def __init__(self,imagePath,speed=2.0,x=0.0,y=0.0):
        self.image = pygame.image.load(imagePath)
        self.speed = speed
        self.position = Vector2(x,y) 
        self.x_axis=0.0
        self.y_axis=0.0
        
        self.momentumX=0.0
        self.momentumY=0.0
                 
        self.left=False
        self.right=False
        self.up=False
        self.down=False
        
    
    def getKey(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left =True
            if event.key == pygame.K_RIGHT:
                self.right =True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left =False
            if event.key == pygame.K_RIGHT:
                self.right =False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.up =True
            if event.key == pygame.K_DOWN:
                self.down =True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.up =False
            if event.key == pygame.K_DOWN:
                self.down =False
       
    def move(self,speedX=None,speedY=None):
        if self.right:
            if self.x_axis<1:
                self.x_axis+=Car.moveStep
        elif self.right == False:
            if self.x_axis>0:
                self.x_axis-=Car.moveStep
               
        if self.left:
            if self.x_axis>-1:
                self.x_axis-=Car.moveStep
        elif self.left == False:
            if self.x_axis<0:
                self.x_axis+=Car.moveStep
            
        if self.down:
            if self.y_axis<1:
                    self.y_axis+=Car.moveStep
        elif self.down == False:
            if self.y_axis>0:
                self.y_axis-=Car.moveStep
            
        if self.up:
            if self.y_axis>-1:
                self.y_axis-=Car.moveStep
        elif self.up == False:
            if self.y_axis<0:
                self.y_axis+=Car.moveStep
        
        if ((self.x_axis > -0.1) and (self.x_axis<0.1)) and (self.left == False and self.right == False):
            self.x_axis = 0.0
        
        if (self.y_axis > -0.1) and (self.y_axis<0.1) and (self.down == False and self.up == False):
            self.y_axis = 0.0
        
        self.position.x+= self.x_axis*self.speed
        self.position.y+= self.y_axis*self.speed
            
    def velocity(self,vector):
        self.momentumX+= Car.moveStep*vector.x*math.cos(math.radians(vector.direction()))-self.position.x
        self.momentumY+= Car.moveStep*vector.y*math.sin(math.radians(vector.direction()))-self.position.y
        
        if(self.momentumX < 0):
            self.momentumX = 0
        
        if(self.momentumY < 0):
            self.momentumY = 0
        
        self.position.x+= Car.moveStep*vector.x*math.cos(math.radians(vector.direction())) + self.momentumX
        self.position.y+= Car.moveStep*vector.y*math.sin(math.radians(vector.direction())) + self.momentumY
        
    def draw(self,gameDisplay):
        gameDisplay.blit(self.image,(self.position.x,self.position.y))
    
    def setLocation(self,vec):
        self.position = vec
    


#car object PRESETS
car1 = Car('car1.png')
car2 = Car('car2.png')
car3 = Car('car3.png')
car4 = Car('pigCar.png')
    