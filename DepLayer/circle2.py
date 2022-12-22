# from ex002 import *
# import matplotlib.pyplot as plt
# import numpy as np
# def circle2 (self, x: float, y: float, r: float):
#     d = self.r*2
#     px = self.x-self.r
#     py = self.y-self.r

#     h = rectangle('Position',[px, py, d, d],'Curvature',[1,1])
#     daspect = [1,1,1]
#     return h

# circle2(1,1,1,1)
###############################################################
 
# x = np.linspace( -0.7 , 0.7 , 150 )
# y = np.linspace( -0.7 , 0.7 , 150 )
 
# a, b = np.meshgrid( x , y )
 
# C = a ** 2 + b ** 2 - 0.2
 
# figure, axes = plt.subplots()
 
# axes.contour( a , b , C , [0] )
# axes.set_aspect( 1 )
 
# plt.show()