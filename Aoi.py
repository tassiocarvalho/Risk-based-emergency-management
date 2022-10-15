import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class CommNet:
    def __init__(self, name, range: float, accPosx: float, accPosy: float, color):
        self.name = name
        self.range = range
        self.accPosx = accPosx
        self.accPosy = accPosy
        self.color = color

    def plotcircle(self):
        plt.plot([0]) 
        plt.title(self.name)
        circle1 = plt.Circle((self.accPosx, self.accPosy), self.range, color=self.color)
        plt.gca().add_patch(circle1)

class Aoi:                                                  #Classe Área de interesse
    def __init__(self, x: float, y: float, h: float, w: float, beta: float):
        self.x = x                       #x
        self.y = y                       #y
        self.h = h                       #altura
        self.w = w                       #comprimento
        self.beta = beta                 #angulo

    def plot(self):
        plt.plot([0])                                       #Plota a figura que irá ser gerada
        plt.title("Aréa")                                   #Titulo da plotagem
        plt.gca().add_patch(Rectangle((self.x, self.y),     #paramentro recebe o ponto incial de onde será o retangulo
                            self.w,self.h,                  #Largura e altura do retangulo
                            angle=self.beta,                #define angulo de retangulo
                            edgecolor='Blue',               #Define cor da borda
                            facecolor='none',               #Define cor da área
                            lw=1))                          #Grossura da borda
        plt.show()                                          #Mostra a imagem

##TESTS##
Circle0 = CommNet("circle", 30, 1, 1, "red")                #Instânciando obejeto communication network
Circle1 = CommNet("circle2", 10, 10, 30, "green")           #Instânciando obejeto communication network
Circle2 = CommNet("circle3", 20, 30, 20, "pink")            #Instânciando obejeto communication network
Circle3 = CommNet("cccc", 10, 0, 0, "blue")                 #Instânciando obejeto communication network
area = Aoi(0,0,30,50,0)                                     #Instânciando obejeto área
Circle0.plotcircle()                                        #Chamando a função para plotar circulo
Circle1.plotcircle()                                        #Chamando a função para plotar circulo
Circle2.plotcircle()                                        #Chamando a função para plotar circulo
Circle3.plotcircle()                                        #Chamando a função para plotar circulo
area.plot()                                                 #Chamando a função para plotar a área