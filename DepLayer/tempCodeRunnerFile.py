from ex002 import *
import matplotlib.pyplot as plt
import numpy as np
def circle2 (self, x: float, d: int, y: float, r: float):
    self.d = r*2
    self.px = x-r
    self.py = y-r

    h = rectangle('Position',[self.px, self.py, self.d],'Curvature',[1,1])
    daspect = [1,1,1]
    return h

circle2(1,1,1,1,1)