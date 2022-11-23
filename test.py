import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math

class AoI:                                                  #Classe Área de interesse
    def __init__(self, x: float, y: float, h: float, w: float, beta: float):
        self.x = x                       #x
        self.y = y                       #y
        self.h = h                       #altura
        self.w = w                       #comprimento
        self.beta = beta                 #angulo

    def plotgrid(self, mArea: float, ws: float, hs: float):
        self.mArea = self.x*self.y
        self.ws = 1
        self.hs = 1
        
        M = self.mArea*self.w/self.ws
        N = self.mArea*self.h/self.hs

        for m in range (10):
            for n in range (10):
                x1s = x1+(m-1)*(self.w/M)*math.cos(math.radians(self.beta)) +(n-1)*(self.h/N)*math.sin(math.radians(self.beta))
                y1s = y1+(m-1)*(self.w/M)*math.sin(math.radians(self.beta))-(n-1)*(self.h/N)*math.cos(math.radians(self.beta))
                x2s = x1+m*(self.w/M)*math.cos(math.radians(self.beta)) + (n-1)*(self.h/N)*math.sin(math.radians(self.beta))
                y2s = y1 + m*(self.w/M)*math.sin(math.radians(self.beta)) - math.cos(math.radians(self.beta))
                x3s = x1 + (m-1)*(self.w/M)*math.cos(math.radians(self.beta))+n*(self.h/N)*math.sin(math.radians(self.beta))
                y3s = y1 + (m-1)*(self.w/M)*math.sin(math.radians(self.beta))-n*(self.h/N)*math.cos(math.radians(self.beta))
                x4s = x1 + m·(self.w/M)*math.cos(math.radians(self.beta))+n*(self.h/N)*math.sin(math.radians(self.beta))
                y4s = y1 + m·(self.w/M)*math.sin(math.radians(self.beta))-n*(self.h/N)*math.cos(math.radians(self.beta))
                xc = x1s + (x4s-x1s)/2
                yc = y1s + (y4s-y1s)/2
                plt.plot([0]) 
                plt.gca().add_patch(Rectangle((1, 1),     #paramentro recebe o ponto incial de onde será o retangulo
                            self.w,self.h,                  #Largura e altura do retangulo
                            angle=self.beta,                #define angulo de retangulo
                            edgecolor='Blue',               #Define cor da borda
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

area = AoI(0,0,30,50,0)
area.plot()