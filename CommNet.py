import matplotlib.pyplot as plt
#communication network
class CommNet:
    def __init__(self, name, range: float, accPosx: float, accPosy: float):
        self.name = name
        self.range = range
        self.accPosx = accPosx
        self.accPosy = accPosy

    def plot(self):
        plt.plot([0]) 
        plt.title(self.name)
        circle1 = plt.Circle((self.accPosx, self.accPosy), self.range, color='blue')
        plt.gca().add_patch(circle1)

        plt.show()

circle1= CommNet("Wifi", 2, 4, 5) 
circle1.plot() 
    