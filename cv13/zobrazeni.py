import abc
from math import cos
# Třída pro reprezentaci zobrazení

class AbstractProjection(abc.ABC):
    @abc.abstractmethod
    def forward(self,lon, lat):
        pass

    @abc.abstractmethod
    def backward(self,x,y):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

class WGS84(AbstractProjection):
    def forward(self,lon,lat):
        return lon,lat
    
    def backward(self,x,y):
        return x,y

    def __str__(self):
        return f"WGS84 projection"

# Dopište zobrazovací rovnice pro Equirectangular projection
# V inicializátoru nastavte atributy R a phi1
class Equirectangular(AbstractProjection):
    def __init__(self,R=6371.11,phi1=0):
        self.R = R
        self.phi1 = phi1
    
    def __str__(self):
        return f"Equirectangular projection with R={self.R} and phi1={self.phi1}"

    def forward(self,lon,lat):
        x = self.R*lon*cos(self.phi1)
        y = self.R*lat
        return x,y

    def backward(self,x,y):
        lon = x/(self.R*cos(self.phi1))
        lat = y/self.R
        return lon,lat

proj = Equirectangular(R=6378)
print(proj.forward(0,10))
print(proj.backward(*proj.forward(13,26)))
print(proj)
