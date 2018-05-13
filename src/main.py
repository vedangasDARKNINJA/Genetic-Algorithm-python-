import math
import numpy as np

class Connection:
    def __init__(self,connectedNeuron):
        self.connectedNeuron = connectedNeuron;
        self.weight = np.random.normal()
        self.dWeight = 0.0
        

class Neuron:
    eta =0.001
    alpha=0.01
    
    #constructor
    def __init__(self,layer):
        self.dendrons = []
        self.error = 0.0
        self.gradient = 0.0
        self.output = 0.0
        
        if(layer is None):
            #if the layer is input layer/bias layer
            pass
        else:
            #make connections
            for neuron in layer:
                con = Connection(neuron)
                self.dendrons.append(con)

    
    #ERROR FUNCTIONS
    def setError(self,newErr):
        self.error = newErr
    
    def addError(self,error):
        self.error+= error
        
    #ACTIVATION FUNCTIONS    
    def sigmoid(self,x):
        return 1.0/(1.0 + np.exp(-x))
    
    def dSigmoid(self,x):
        return x * (1.0 - x)
    
    #OUTPUT
    def getOutput(self):
        return self.output
    def setOutput(self,output):
        self.output = output
        
        
        
    #FEED FORWARD
    def feedForward(self):
        sumOutput = 0
        if len(self.dendrons) == 0:
            return
        for dendron in self.dendrons:
            sumOutput = sumOutput + float(dendron.connectedNeuron.getOutput()) * dendron.weight
        self.output = self.sigmoid(sumOutput)
        
    #BACK PROPAGATION
    def backPropagate(self):
        self.gradient = self.error * self.dSigmoid(self.output);
        for dendron in self.dendrons:
            dendron.dWeight = Neuron.eta * (
            dendron.connectedNeuron.output * self.gradient) + self.alpha * dendron.dWeight;
            dendron.weight = dendron.weight + dendron.dWeight;
            dendron.connectedNeuron.addError(dendron.weight * self.gradient);
        self.error = 0;
        
        
class Network:
    def __init__(self,topology):
        self.layers = []
        for numNeuron in topology:
            layer = []
            for i in range(numNeuron):
                if(len(self.layers)==0):
                    layer.append(Neuron(None))
                else:
                    layer.append(Neuron(self.layers[-1]))
            layer.append(Neuron(None))
            layer[-1].setOutput(-1)
            self.layers.append(layer)
            
    def setInput(self,inputs):
        for i in range(len(inputs)):
            self.layers[0][i].setOutput(inputs[i])
            
    def getError(self,target):
        err = 0
        #ROOT MEAN SQUARE ERROR
        for i in range(len(target)):
            e = (target[i]-self.layers[-1][i].getOutput())
            err = err+ e**2     #SQUARED
        err = err/len(target)       #MEAN
        err = math.sqrt(err)    #ROOT
        return err
    
    #feed forward in network
    def feedForward(self):
        for layer in (self.layers[1:]):
            for neuron in layer:
                neuron.feedForward();
                
                
    #back propagate in network
    def backPropagate(self, target):
        for i in range(len(target)):
            self.layers[-1][i].setError(target[i] - self.layers[-1][i].getOutput())
        for layer in self.layers[::-1]:
            for neuron in layer:
                neuron.backPropagate()
                
    #get the results
    def getThResults(self):
        output = []
        for neuron in self.layers[-1]:
            o = neuron.getOutput()
            output.append(o)
        output.pop()# removing the bias neuron
        return output
    
    
def main():
    topology = []
    topology.append(2)
    topology.append(3)
    topology.append(1)
    
    net = Network(topology)
    Neuron.eta = 0.09
    Neuron.alpha =0.015
    
    while True:
        err = 0
        inputs = [[0, 0, 0], [0, 0, 1], [1, 0, 0], [1, 1, 0]]
        outputs = [[0],[1],[1],[0]]
        for i in range(len(inputs)):
            net.setInput(inputs[i])
            net.feedForward()
            print("Results for input %d %d %d : " %(inputs[i][0],inputs[i][1], inputs[i][2]),net.getThResults())
            net.backPropagate(outputs[i])
            err = err + net.getError(outputs[i])
        print ("error: ", err)        
        if(err < 0.01):
            break
    
    while True:
        a = input("type 1st input :")
        b = input("type 2nd input :")
        c = input("type 3rd input :")
        net.setInput([a,b,c])
        net.feedForward()
        print (net.getThResults())
    

if __name__ == '__main__':
    main()