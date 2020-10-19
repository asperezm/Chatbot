from Correlacion import *

class UnidadDialogo:
  #metodos
  def __init__(self, nombreUnidad):
    self.nombreUnidad = nombreUnidad
    self.preguntas = []
    self.respuestas = []

  def addPregunta(self, texto):
    self.preguntas.append(texto.lower())

  def addRespuesta(self, texto):
    self.respuestas.append(texto.lower())

  def validarGrupo(self, texto):
    relacion = 0;
    for frase in self.preguntas:
      frase.strip().lower()
      texto.strip().lower()
      igual = levenshtein_proporcion_distancia(texto,frase, True)
      if(relacion < igual):
        relacion = igual
    return relacion

  def darRespuesta(self):
    import random
    i = random.randint(0,len(self.respuestas)-1)
    return self.respuestas[i]

  def getPreguntas(self):
    return self.preguntas

  def getRespuestas(self):
    return self.respuestas
