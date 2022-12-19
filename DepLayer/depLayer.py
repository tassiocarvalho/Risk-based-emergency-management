import os
import numpy
import numpy as np
import numpy.ma as ma
from ex002 import *
import ex002
from circle2 import *
ex=2

WINDOWS = 0
LINUX = 1

opSys = WINDOWS
#opSys = LINUX

if (opSys == WINDOWS):
        ex002
elif (opSys == LINUX):
        ex002
else:
    print("Sistema operacional não definido")

#placeRandomNetworks #<-- ainda implementar
totalNets = sum(nNets)   #pegando o valor da variavel nNets no ex002 e somando todos valores da lista

wMBs = int(w/sizeMB)
hMBs = int(h/sizeMB)
ws = w/wMBs
hs = h/hMBs
M = wMBs
N = hMBs

CTSR=0 #Valor máximo da função objetivo, considerando uma região com todas as redes sobrepostas

for i in range(len(paramNets)):
    CTSR = CTSR - paramNets[i].c + paramNets[i].t + paramNets[i].s + paramNets[i].r

##PLOT INICIAL
color = np.array(['k' ,'b' ,'m' ,'c'])
nC = ma.size(color)

# if (PLOT_GRAPHS == 1):
#     cLegends = []
#     iNets = []

#     for i in range(len(networks)):
#         graphCircle = cric#circle2(networks(i,2), networks(i,3),paramNets( networks(i,1) ).R)
#         set(graphCircle,'LineStyle','-','LineWidth',1.5,'EdgeColor',color(mod( networks(i,1),nC )+1))

        #if (networks[i] in iNets):
            #iNets.append(networks[i])
            #hline = plot(NaN,NaN,'LineWidth',1.5,'LineStyle','-','Color',color(mod( networks(i,1),nC )+1))
            #cLegends.append(paramNets[networks[i]].name)

MBs = np.zeros((hMBs,wMBs),float)
MBs_classes = np.zeros((hMBs,wMBs),float)
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

        connLevel = 0
        #for i in range(len(networks)):
         #    inn, dist = isWithinNet( xc, yc, networks[i], paramNets[networks[i].R] )
             
          #   if (inn):
           #     connLevel = connLevel + (-C*paramNets(networks[i]).c + T*paramNets(networks[i]).t + S*paramNets(networks[i].s) + R*paramNets(networks[i].r))/CTSR;

        #MBs(mIndex,nIndex) = connLevel

        #if (connLevel < connLevelMin):
            #MBs_classes(nIndex,mIndex) = 0
        #else: 
            #for i in range(nConnLevels):
                #if( connLevel >= connLevelRange(i) and connLevel < connLevelRange(i+1)):
                    #if (PLOT_GRAPHS == 1):
                        #rectangle('Position',[x3s, y3s, ws, hs],'LineWidth',0.5,'EdgeColor',levelColors[i],'FaceColor',levelColors[i])

                        #MBs_classes(nIndex,mIndex) = i

        #if(PLOT_GRAPHS and PLOT_MBS == 1):
         #   grayColor = [.7, .7, .7]
          #  line([x1s, x2s],[y1s, y2s],'Color',grayColor,'LineStyle',':','LineWidth',1.0)
           # line([x2s, x4s],[y2s, y4s],'Color',grayColor,'LineStyle',':','LineWidth',1.0)
            #line([x4s, x3s],[y4s, y3s],'Color',grayColor,'LineStyle',':','LineWidth',1.0)
            #line([x3s, x1s],[y3s, y1s],'Color',grayColor,'LineStyle',':','LineWidth',1.0)

x2 = x1 + w*cosBeta
y2 = y1 + w*sinBeta
x3 = x1 + h*sinBeta
y3 = y1 - h*cosBeta
x4 = x1 + h*sinBeta + w*cosBeta
y4 = y1 - h*cosBeta + w*sinBeta


#if(PLOT_GRAPHS):
#    line([x1,x2],[y1,y2],'Color','k')
#    line([x2,x4],[y2,y4],'Color','k')
#    line([x4,x3],[y4,y3],'Color','k')
#    line([x3,x1],[y3,y1],'Color','k')
#    legend(cLegends)

#if(PLOT_GRAPHS):
    #for i in range(networks):
        #graphCircle = circle2(networks(i,2), networks(i,3),paramNets( networks(i,1) ).R)
       #set(graphCircle,'LineStyle',':','LineWidth',1.5,'EdgeColor',color(mod( networks(i,1),nC )+1))
#legend(cLegends)
