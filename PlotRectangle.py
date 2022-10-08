#Algoritmo em python que plota uma área de um retângulo 
#podendo definir angulo, largura e altura e posição
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

p1 = int(input("informe o ponto inicial do retângulo X: "))
p2 = int(input("informe o ponto final do retângulo Y: "))
larg = int(input("informe a largura do retangulo: : "))
alt = int(input("informe a altura do retângulo: "))
ag = input("informe o Valor do ângulo da área: ")

f1 = plt.figure()                       #Plota a figura inicial
plt.plot([0])                           #Plota a figura que irá ser gerada
plt.title("Aréa")                       #Titulo da plotagem
plt.gca().add_patch(Rectangle((p1,p2),    #paramentro recebe o ponto incial de onde será o retangulo
                    larg,alt,                  #Largura e altura do retangulo
                    angle=ag,            #define angulo de retangulo
                    edgecolor='Blue',   #Define cor da borda
                    facecolor='green',  #Define cor da área
                    lw=1))              #Grossura da borda
plt.show()                              #Mostra a imagem
