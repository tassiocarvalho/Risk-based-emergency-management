import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

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
##Test##
area = Aoi(0,0,40,50,35)                      #Instanciando objeto
area.plot()                                                 #chamando metodo plot para o objeto instaciado