import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math

mArea = 100
w = 10
h = 10
ws = 3
hs = 3 
beta = 0
x1 =0
y1 =0

m =1
n =1

M = 4
N = 5

for x1 in range (9):
    for y1 in range (16):

        (x1+1)
        (y1+1)
        plt.plot()                                       #Plota a figura que irá ser gerada
        plt.title("Área")                                   #Titulo da plotagem
        plt.gca().add_patch(Rectangle((x1, y1),     #paramentro recebe o ponto incial de onde será o retangulo
                                    ws,hs,                  #Largura e altura do retangulo
                                    angle=0,                #define angulo de retangulo
                                    edgecolor='Blue',               #Define cor da borda
                                    facecolor='none',               #Define cor da área
                                    lw=1))                          #Grossura da borda
plt.show()                                                          #Mostra a imagem