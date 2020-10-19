from UnidadDialogo import *
from Dialogos import *
from Nodo import *
from Metodos import *

def iniciarChat():
  lista = []
  udSaludos = cargarUnidad("Saludos", "corpus_saludos.txt")
  udDespedidas=cargarUnidad("Despedidas", "corpus_despedidas.txt")
  udUrgencia=cargarUnidad("Urgencia", "corpus_urgencia.txt")
  udCita = cargarUnidad("Cita", "corpus_citas.txt")
  udMed = cargarUnidad("medicamentos", "corpus_medicamentos.txt")
  udTar = cargarUnidad("tarifa", "corpus_tarifas.txt")
  udOri = cargarUnidad("orientacion", "corpus_orientacion.txt")

  print(" Asistente: Hola, en que puedo ayudarte?")

  while True:
    Pregunta = input("> ")
    humano = Pregunta.lower()
    salu = Nodo("Saludo",udSaludos.validarGrupo(humano))
    desp =Nodo("Despedida",udDespedidas.validarGrupo(humano))
    urg = Nodo("Urgencia",udUrgencia.validarGrupo(humano))
    cita = Nodo("cita",udCita.validarGrupo(humano))
    med = Nodo("Medicamentos",udMed.validarGrupo(humano))
    ori = Nodo("orientacion",udOri.validarGrupo(humano))
    tar = Nodo("tarifa",udTar.validarGrupo(humano))

    lista.append(salu)
    lista.append(desp)
    lista.append(urg)
    lista.append(cita)
    lista.append(med)
    lista.append(ori)
    lista.append(tar)
    Punt = PuntajeMax(lista)

    NombreGan = Punt.getNombre()
    if NombreGan == "Saludo":
      print("  Asistente: ", udSaludos.darRespuesta())
    elif NombreGan == "Urgencia":
      print("  Asistente: ", udUrgencia.darRespuesta())
    elif NombreGan == "cita":
      print("  Asistente: ", udCita.darRespuesta())
    elif NombreGan == "Medicamentos":
      print("  Asistente: ", udMed.darRespuesta())
    elif NombreGan == "tarifa":
      print("  Asistente: ", udTar.darRespuesta())
    elif NombreGan == "orientacion":
      print("  Asistente: ", udOri.darRespuesta())
    elif NombreGan == "Despedida":
      print("  Asistente: ", udDespedidas.darRespuesta())
      break
    else:
       print("  Asistente: no te entiendo, podrias decirlo mejor?")
    lista.clear()
    print()
  print("... El chat se cerro")



