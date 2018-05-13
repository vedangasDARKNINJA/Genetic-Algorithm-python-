import numpy as np
from Vectors import Vector2

class DNA:
    def __init__(self,genomeLength=50,parent=None,partner=None,mutationRate=0.4):
        self.PositionGenes = []
        if((parent==None)and(partner==None)):
            for i in range(genomeLength):
                vec = Vector2(np.random.uniform(-1.0,1.0),np.random.uniform(-1.0,1.0))
                self.PositionGenes.append(vec)
            
        else:
            if ((parent!=None) and (partner != None)):            
                for i in range(genomeLength):
                    if(i<10):
                        if(np.random.uniform(0.0,1.0)<= mutationRate):
                            self.PositionGenes.append(parent.PositionGenes[i] + Vector2(np.random.uniform(-0.05,0.05),np.random.uniform(-0.05,0.05)))
                        else:
                            self.PositionGenes.append(partner.PositionGenes[i] + Vector2(np.random.uniform(-0.05,0.05),np.random.uniform(-0.05,0.05)))
                    else:
                        if(np.random.uniform(0.0,1.0)>mutationRate):
                            self.PositionGenes.append(parent.PositionGenes[i])
                        else:
                            self.PositionGenes.append(partner.PositionGenes[i])
                    
    def printGene(self):
        print("GENE LENGTH:",len(self.PositionGenes))
        for i in range(len(self.PositionGenes)):
            print("Gene[",i,"]: ",self.PositionGenes[i])