from ex002 import *
import ex002
import numpy as np

offset = 50

xMax = max([x1,x2,x3,x4])
xMin = min([x1,x2,x3,x4])
yMax = max([y1,y2,y3,y4])
yMin = min([y1,y2,y3,y4])

for i in range(len(nNets)):
    for j in range(nNets[i]):
        st = xMin+offset
        sp = xMax-offset
        qtt = 1
        sx = np.random.uniform((sp,(sp-st),(qtt)))+st

        APx = sx

        st = yMin+offset
        sp = yMax-offset
        qtt = 1
        sy = np.random.uniform((sp,(sp-st),(qtt)))+st
        
        APy = sy

        APi = [APx, APy]
        networks.append(APi)

        print(networks)
        