from random import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

color = ['r','g','b']

class CommNet:                                              #Classe communication network
    def __init__(self, name, range: float, accPosx: float, accPosy: float, color):
        self.name = name
        self.range = range
        self.accPosx = accPosx
        self.accPosy = accPosy
        self.color = color

    def plotcircle(self):
        plt.plot([0]) 
        plt.title(self.name)
        circle1 = plt.Circle((self.accPosx, self.accPosy), self.range, color=self.color,alpha=.4)
        plt.gca().add_patch(circle1)

for i in range(10):
    Circle0 = CommNet("aaa", 20 * random(), 100 * random(), 20 * random(), "r")                #Instânciando obejeto communication network

    Circle0.plotcircle()                                        #Chamando a função para plotar circulo
