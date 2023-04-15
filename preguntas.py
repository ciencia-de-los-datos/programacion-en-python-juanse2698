"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
from csv import reader
file = open("data.csv","r")
archivo = reader(file,delimiter= "\t")
archivo = list(archivo)

def pregunta_01():
    sumatoria = 0
    for fila in archivo:
        sumatoria += int(fila[1])
    return sumatoria

def pregunta_02():
    
    columna = [fila[0] for fila in archivo]
    columna_no_duplicadas = sorted(set(columna))
    lista_tupla =[(j, columna.count(j)) for j in columna_no_duplicadas]
    return lista_tupla
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    


def pregunta_03():
    datos = [(row[0], int(row[1])) for row in archivo]
    sumas = {}
    for letra, numero in datos:
        if letra in sumas:
            sumas[letra] += numero
        else:
            sumas[letra] = numero
    result = sorted(sumas.items())
    return result

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return


def pregunta_04():
    counts = [0] * 12
    for row in archivo:
        fecha_str = row[2]
        año, mes, dia = fecha_str.split('-')
        mes_index = int(mes) - 1
        counts[mes_index] += 1
    result = [(f"{i+1:02d}", count) for i, count in enumerate(counts)]
    return result
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return


def pregunta_05():
    max_min_dict = {}
    for row in archivo:
        letra = row[0]
        valor = float(row[1])
        if letra not in max_min_dict:
            max_min_dict[letra] = {'max': valor, 'min': valor}
        else:
            max_min_dict[letra]['max'] = max(max_min_dict[letra]['max'], valor)
            max_min_dict[letra]['min'] = min(max_min_dict[letra]['min'], valor)

    result = [(letra, max_min_dict[letra]['max'], max_min_dict[letra]['min']) for letra in sorted(max_min_dict)]
    return result
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return


def pregunta_06():
    min_max_dict = {}
    for row in archivo:
        col5 = row[4]
        if col5 != "":
            for pair in col5.split(","):
                llave, valor = pair.split(":")
                if llave not in min_max_dict:
                    min_max_dict[llave] = {'min': float(valor), 'max': float(valor)}
                else:
                    min_max_dict[llave]['min'] = min(min_max_dict[llave]['min'], float(valor))
                    min_max_dict[llave]['max'] = max(min_max_dict[llave]['max'], float(valor))

    result = [(llave, min_max_dict[llave]['min'], min_max_dict[llave]['max']) for llave in sorted(min_max_dict)]
    return result
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return


def pregunta_07():
    dict_valor = {}
    for row in archivo:
        col1 = row[0]
        col2 = row[1]
        if col2 not in dict_valor:
            dict_valor[col2] = [col1]
        else:
            dict_valor[col2].append(col1)

    result = [(int(llave), dict_valor[llave]) for llave in sorted(dict_valor)]
    return result
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    dict_valor = {}
    for row in archivo:
        col1 = row[0]
        col2 = row[1]
        if col2 not in dict_valor:
            dict_valor[col2] = [col1]
        else:
            dict_valor[col2].append(col1)
    result = [(int(llave), sorted(list(set(dict_valor[llave])))) for llave in sorted(dict_valor)]
    return result
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    dict_contador = {}
    for row in archivo:
        col5 = row[4]
        for llave_value in col5.split(','):
            llave = llave_value[:3]  # Obtiene la clave de tres letras
            if llave in dict_contador:
                dict_contador[llave] += 1
            else:
                dict_contador[llave] = 1
    return dict_contador
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    lista_contador = []
    for row in archivo:
        col1 = row[0]
        col4 = row[3]
        col5 = row[4]
        contador4 = len(col4.split(',')) 
        contador5 = len(col5.split(','))
        lista_contador.append((col1, contador4, contador5))
    return lista_contador
        

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    result = {}
    for row in archivo:
        col2 = int(row[1])
        col4 = row[3].split(',')
        for letra in col4:
            letra = letra.strip()  # elimina espacios en blanco antes y después de la letra
            if letra not in result:
                result[letra] = col2
            else:
                result[letra] += col2

    result = dict(sorted(result.items()))  # ordena el diccionario por clave
    return result

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    diccionario_resultado = {}
    for linea in archivo:
        letra = linea[0]
        dic_codificado = linea[4]
        diccionario = {}
        for item in dic_codificado.split(','):
            clave, valor = item.split(':')
            diccionario[clave] = int(valor)
            suma = sum(diccionario.values())
        diccionario_resultado[letra] = diccionario_resultado.get(letra, 0) + suma
    return diccionario_resultado

    
   