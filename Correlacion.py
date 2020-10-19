import numpy as np

def levenshtein_proporcion_distancia(textoBase, textoFuente, medir_proporcion = False):
    """ Levenshtein_porporcion_and_mDistancias:
        Calcula la distancia levenshtein entre dos expresiones.
        
        medir_proporcion = True calcular la función de
        relación de distancia levenshtein de similitud entre dos expresiones
        
        Para todo i y j, la distancia [i, j] contendrá el Levenshtein
        distancia entre los primeros i caracteres del textoBase y los 
        primeros caracteres j del textoFuente
    """
    # Crea una matriz de ceros
    filas = len(textoBase)+1
    cols = len(textoFuente)+1
    mDistancias = np.zeros((filas,cols),dtype = int)

    # Matriz de ceros entre textoBase con textoFuente, encabezado con numero
    for i in range(1, filas):
        for k in range(1,cols):
            mDistancias[i][0] = i
            mDistancias[0][k] = k


    # iterar sobre la matriz para calcular el valor de las eliminaciones, inserciones y / o sustituciones
    for col in range(1, cols):
        for fila in range(1, filas):
            if textoBase[fila-1] == textoFuente[col-1]:
                valor = 0 # Si los caracteres son iguales en las dos cadenas en una posición dada [i, j], entonces el valor es 0
            else:
                if medir_proporcion == True:
                    valor = 2  #Si desea calcular la proporción, si son diferentes, el valor es 2 por sustitución
                else:
                    valor = 1  #Si desea calcular la distancia, si son diferentes, el valor es 1 por sustitución
            mDistancias[fila][col] = min(mDistancias[fila-1][col] + 1,  # valor de borrado
                                 mDistancias[fila][col-1] + 1,          # valor de inserciones
                                 mDistancias[fila-1][col-1] + valor)     # valor de sustituciones

    if medir_proporcion == True:
        # Cálculo de la relación de distancia de Levenshtein
        porporcion = ((len(textoBase)+len(textoFuente)) - mDistancias[fila][col]) / (len(textoBase)+len(textoFuente))
        #print('matriz de calculos proporcion: ')
        #print(mDistancias)
        #print('(',(len(textoBase)+len(textoFuente)),'-', mDistancias[fila][col],')/',len(textoBase)+len(textoFuente),'=',porporcion)
        return porporcion
        #return "Las expresiones tienen una proporción de igualdad del {}%".format(porporcion)
    else:
        #print('matriz de calculos distancia: ')
        #print(mDistancias)
        #print('distancia[',fila,'][',col,']: ',mDistancias[fila][col])
        return mDistancias[fila][col]
        #return "Las expresiones estan distantes en {} unidades de correlación. A menor la distancia, mayor la dependencia estocástica". format(mDistancias[fila][col])