import circle
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

circle
        
class AoI:                                                  #Classe Área de interesse
    def __init__(self, x: float, y: float, h: float, w: float, beta: float):
        self.x = x                       #x
        self.y = y                       #y
        self.h = h                       #altura
        self.w = w                       #comprimento
        self.beta = beta                 #angulo
        #MBs[[]]

    def plot(self):
        plt.plot([0])                                       #Plota a figura que irá ser gerada
        plt.title("Área")                                   #Titulo da plotagem
        plt.gca().add_patch(Rectangle((self.x, self.y),     #paramentro recebe o ponto incial de onde será o retangulo
                            self.w,self.h,                  #Largura e altura do retangulo
                            angle=self.beta,                #define angulo de retangulo
                            edgecolor='Blue',               #Define cor da borda
                            facecolor='none',               #Define cor da área
                            lw=1))                          #Grossura da borda
        plt.show()                                          #Mostra a imagem

##TESTS##

area = AoI(0,0,20,100,0)                                     #Instânciando obejeto área
area.plot()                                                 #Chamando a função para plotar a área