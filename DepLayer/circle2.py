from ex002 import *
import matplotlib.pyplot as plt

def circle2 (self, x: float, y: float, r: float):
    self.d = r*2
    self.px = x-r
    self.py = y-r

    h = rectangle('Position',[self.px, self.py, self.d, self.d],'Curvature',[1,1])
    daspect = [1,1,1]
    return h

circle2(1,1,1,1)
###############################################################

