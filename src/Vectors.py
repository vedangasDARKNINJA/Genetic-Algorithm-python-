import math

class Vector2:
    
    @staticmethod   
    def Distance(vec1,vec2):
        distance = math.hypot(vec1.y-vec2.y, vec1.x-vec2.x)
        return distance
    
    @staticmethod
    def MoveToward(currentPos,targetPos,maxDistanceDelta):
        delta = targetPos-currentPos
        magnitude = delta.magnitude()
        if (magnitude <= maxDistanceDelta or magnitude == 0.0):
            return targetPos
        return currentPos + (delta.normalised()* maxDistanceDelta) 
    
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x,y)
    def __sub__(self,other):
        x = self.x-other.x
        y = self.y-other.y
        return Vector2(x,y)
    def __mul__(self,magnitude):
        return Vector2(self.x*magnitude,self.y*magnitude)
    def __eq__(self,other):
        if((self.x == other.x)and(self.y==other.y)):
            return True
        return False
    def __ne__(self,other):
        if(self.x == other.x)and(self.y==other.y):
            return False
        return True
    
    def magnitude(self):
        return (math.sqrt(self.x**2+self.y**2))
     
    def direction(self,center=None):
        if center is None:
            return math.degrees(math.atan2(self.y,self.x))
        else:
            return math.degrees(math.atan2(self.y-center.y,self.x-center.x))
    
    def normalised(self):
        vec = Vector2()
        if(self.magnitude() != 0):
            vec = Vector2((self.x/self.magnitude()),(self.y/self.magnitude()))
        return vec

    def asArray(self):
        return [self.x,self.y]
    
zero = Vector2(0,0)
up = Vector2(0,1)
right = Vector2(1,0)