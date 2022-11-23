import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

class AoI:                                                  #Classe Área de interesse
    def __init__(self, x: float, y: float, h: float, w: float, beta: float):
        self.x = x                       #x
        self.y = y                       #y
        self.h = h                       #altura
        self.w = w                       #comprimento
        self.beta = beta                 #angulo

    def plotgrid(self):
        plt.plot([0])
        plt.gca().add_patch(Rectangle((self.x, self.y),     #paramentro recebe o ponto incial de onde será o retangulo
                            1,1,                  #Largura e altura do retangulo
                            angle=self.beta,                #define angulo de retangulo
                            edgecolor='red',               #Define cor da borda
                            facecolor='none',               #Define cor da área
                            lw=1))
    def plotgrid2(self):
        plt.plot([0])
        plt.gca().add_patch(Rectangle((self.x+1, self.y+1),     #paramentro recebe o ponto incial de onde será o retangulo
                            1,1,                  #Largura e altura do retangulo
                            angle=self.beta,                #define angulo de retangulo
                            edgecolor='red',               #Define cor da borda
                            facecolor='none',               #Define cor da área
                            lw=1))

    def plot(self):
        plt.plot([0])                                       #Plota a figura que irá ser gerada
        plt.title("Área")                                   #Titulo da plotagem
        plt.gca().add_patch(Rectangle((self.x, self.y),     #paramentro recebe o ponto incial de onde será o retangulo
                            self.w,self.h,                  #Largura e altura do retangulo
                            angle=self.beta,                #define angulo de retangulo
                            edgecolor='Blue',               #Define cor da borda
                            facecolor='none',               #Define cor da área
                            lw=1))                          #Grossura da borda             
        plt.show() 

area = AoI(20,-20,30,50,0)
area.plotgrid()
area.plotgrid2()
area.plot()

