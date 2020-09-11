#!/usr/bin/python3
import math
import matplotlib.pyplot as plt

class Circle:
    @staticmethod
    def circumference(radius):
        return math.pi * 2 * radius

    """
    Returns the radius of the cap, from a given distance h
    from the top of the sphere
    """
    def cap(self, height):
        if height <= 0 or height > 2*self.radius:
            return 0
        capradius =  math.sqrt(2 * self.radius * height - height**2)
        return capradius
        #return self.circumference(capradius)

    """
    returns sin(theta)
    """
    def thetacap(self, height):
        return self.cap(height)/self.radius



    def __init__(self, radius):
        self.radius = radius
        #self.circumference = self.circumference(radius)



def main():
    radius = 10  # nb rows/2 ie resolution
    scale = 6 # size of the sphere
    acc2 = []
    acc = []
    for i in range(1, radius*2):
        acc2.append(math.sin((i*math.pi)/(radius*2+1)))

    acc2 = [x*(scale/min(acc2)) for x in acc2]
    acc2 = [round(x) for x in acc2]

    print(acc2)

    plt.plot(acc2)
    plt.show()

main()
