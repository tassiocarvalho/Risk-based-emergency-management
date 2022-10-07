#Algoritmo em python que plota uma área de um retângulo 
#podendo definir angulo, largura e altura e posição
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

f1 = plt.figure()                       #Plota a figura inicial
plt.plot([0])                           #Plota a figura que irá ser gerada
plt.title("Aréa")                       #Titulo da plotagem
plt.gca().add_patch(Rectangle((0,0),    #paramentro recebe o ponto incial de onde será o retangulo
                    40,80,              #Largura e altura do retangulo
                    angle=0,            #define angulo de retangulo
                    edgecolor='Blue',   #Define cor da borda
                    facecolor='green',  #Define cor da área
                    lw=1))              #Grossura da borda
plt.show()                              #Mostra a imagem