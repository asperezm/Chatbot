from UnidadDialogo import *

def cargarUnidad(nombreUnidad, nombreArchivo):
  ud = UnidadDialogo(nombreUnidad)
  archivo = open(nombreArchivo, "r")
  grupo = 'n'
  
  for linea in archivo:
    linea = linea.rstrip('\n')
    if linea == "<preguntas>":
      grupo = 'p'
    elif linea == "<respuestas>":
      grupo = 'r'
    else:
      if grupo == 'p':
        ud.addPregunta(linea.lower())
      if grupo == 'r':
        ud.addRespuesta(linea.lower())
  return ud