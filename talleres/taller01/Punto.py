
import math
class Punto2D:
    """Representacion de punto en 2 dimensiones"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
    		return self.y

    def radio_polar(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    def angulo_polar(self, x, y):
        angulo = math.atan2(y,x)
        return math.radians(angulo)

    def dist_euclidiana(self, other):
         return math.sqrt(((other.get_x() - self.x)**2)+((other.get_y() -self.y)**2))

p1 = Punto2D(10,20)
p2 = Punto2D(0,0)
print(p1.get_x()) 
print(p1.get_y())
print(p1.radio_polar())
print(p1.angulo_polar(10,20))
print(p1.dist_euclidiana(p2))