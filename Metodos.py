from Nodo import *

def PuntajeMax(puntaje):
    max = Nodo(" ", 0)
    poco = Nodo("poco",10)
    iguales = Nodo("Iguales",100000)
    for a  in puntaje:
      if max.getPuntaje() == a.getPuntaje():
        return iguales
      if max.getPuntaje() < a.getPuntaje():
        max = a
    if max.getPuntaje() < 0.8:
      max = iguales
    return max
