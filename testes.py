import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import math
sizeMB = 3
h = 10
w = 20
x1 = 10
y1 = 10
beta = 0
mIndex = 20
nIndex = 10
wMBs = int(w/sizeMB)
hMBs = int(h/sizeMB)
M = wMBs
N = hMBs
sinBeta = math.sin(math.radians(beta))
cosBeta = math.cos(math.radians(beta))

for mIndex in range(wMBs):
    for nIndex in range(hMBs):
        x1s = x1 + (mIndex-1)*(w/M)*cosBeta + (nIndex-1)*(h/N)*sinBeta
        y1s = y1 + (mIndex-1)*(w/M)*sinBeta - (nIndex-1)*(h/N)*cosBeta
        x2s = x1 + (mIndex)*(w/M)*cosBeta + (nIndex-1)*(h/N)*sinBeta
        y2s = y1 + (mIndex)*(w/M)*sinBeta - (nIndex-1)*(h/N)*cosBeta
        x3s = x1 + (mIndex-1)*(w/M)*cosBeta + (nIndex)*(h/N)*sinBeta
        y3s = y1 + (mIndex-1)*(w/M)*sinBeta - (nIndex)*(h/N)*cosBeta
        x4s = x1 + (mIndex)*(w/M)*cosBeta + (nIndex)*(h/N)*sinBeta
        y4s = y1 + (mIndex)*(w/M)*sinBeta - (nIndex)*(h/N)*cosBeta
        
        xc = x1s + (x4s-x1s)/2
        yc = y1s + (y4s-y1s)/2

        plt.plot([0])                                       #Plota a figura que irá ser gerada
        plt.title("Área")                                   #Titulo da plotagem
        plt.gca().add_patch(Rectangle((x1s, y1s),     #paramentro recebe o ponto incial de onde será o retangulo
                            w,h,                  #Largura e altura do retangulo
                            beta,                #define angulo de retangulo
                            edgecolor='green',               #Define cor da borda
                            facecolor='none',               #Define cor da área
                            lw=1))                          #Grossura da borda

plt.plot([0])                                       #Plota a figura que irá ser gerada
plt.title("Área")                                   #Titulo da plotagem
plt.gca().add_patch(Rectangle((x1, y1),     #paramentro recebe o ponto incial de onde será o retangulo
                    w,h,                  #Largura e altura do retangulo
                    beta,                #define angulo de retangulo
                    edgecolor='red',               #Define cor da borda
                    facecolor='none',               #Define cor da área
                    lw=1))                          #Grossura da borda
plt.show()     