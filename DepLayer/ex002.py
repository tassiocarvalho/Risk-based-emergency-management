import math
from ypstruct import struct
import numpy as np

#######################################################
#####                Váriaveis                   ######
#######################################################
PLOT_GRAPHS = 1
PLOT_MBS = 0
print("ex002 foi aberta!!")
h = 4000                   
w = 10000

x1 = 500
y1 = 500
beta = 30*math.pi/180
sinBeta = math.sin(math.radians(beta))
cosBeta = math.cos(math.radians(beta))

x2 = x1 + w*cosBeta
y2 = y1 + w*sinBeta
x3 = x1 + h*sinBeta
y3 = y1 - h*cosBeta
x4 = x1 + h*sinBeta + w*cosBeta
y4 = y1 - h*cosBeta + w*sinBeta

sizeMB = 50

####################################################
####             DEFININDO NETWORKS             ####
####################################################

paramNets = []     #lista de parametros de cada rede
networks = []      #Lista de redes

netMin = 1
netMax = 5

#NETWORK 1
Rn1 = 100   #metros do alcance da rede
nm1 = "WiFi"    #nome da rede
c1 = 2  #valor
t1 = 4  #taxa de transferencia
s1 = 5  #nível de segurança
r1 = 4  #confiabilidade

#paramNets = concat[paramNets , struct(R=Rn1, name=nm1, c=c1, t=t1, s=s1, r =r1)]

paramNets.append({'R': Rn1, 'name':nm1, 'c':c1, 't':t1, 's':s1, 'r' :r1})

#NETWORK 2 5G
Rn2 = 400       #metros do alcance da rede
nm2 = "5G"      #nome da rede
c2 = 5          #valor
t2 = 5          #taxa de transferencia
s2 = 3          #nível de segurança
r2 = 2          #confiabilidade


paramNets.append({'R': Rn2, 'name':nm2, 'c':c2, 't':t2, 's':s2, 'r' :r2})

#Network 3 - 6LoWPAN
Rn3 = 150  #metros do alcance da rede
nm3 = "6LoWPAN"
c3 = 3
t3 = 3
s3 = 2
r3 = 3

paramNets.append({'R': Rn3, 'name':nm3, 'c':c3, 't':t3, 's':s3, 'r' :r3})

#Network 4 - LoRa
Rn4 = 2500
nm4 = "LoRa"
c4 = 5
t4 = 1
s4 = 2
r4 = 4
paramNets.append({'R': Rn4, 'name':nm4, 'c':c4, 't':t4, 's':s4, 'r' :r4}) #poo

nNets = [100, 30, 50, 2]
#PARÂMETROS DA FUNÇÃO OBJETIVO

C = 1 #'C'ost
T = 1 #'T'hroughput
S = 1 #'S'ecurity
R = 1 #'R'eliability 

#NÍVEIS DE CONECTIVIDADE

nConnLevels = 3

constConnLevels= np.arange(0,nConnLevels+1)
print(constConnLevels)
connLevelMin = 0.00001

connLevelRange= np.arange(connLevelMin,1,(1 - connLevelMin) / nConnLevels)
print(connLevelRange)
levelSum = nConnLevels*(1+nConnLevels)/2

levelColors = ['r','y','g']

nEDUs = 150