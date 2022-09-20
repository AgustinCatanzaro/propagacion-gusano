import networkx as nx
from collections import Counter
import re

def crearGrafo(vertices, aristas):
    myGrafo = nx.Graph()
    myGrafo.add_nodes_from(vertices)
    myGrafo.add_weighted_edges_from(aristas)
    #print('Vertices del Grafo:\n', myGrafo.nodes, '\nAristas:\n', aristas)
    return myGrafo

def nodoDijkstra(miGrafo, nodoInfectado):
    pathsWeight = {}

    for nodo in nodoInfectado:
        paths = nx.single_source_dijkstra_path(miGrafo, nodo[0])
        # Crea un diccionario con todos los caminos posibles para cada nodo que se da como parametro(nodo infectado)
        for singlePath in paths.values():
            if nx.path_weight(miGrafo, singlePath, 'weight') == nodo[1]:
                # Con el diccionario previamente creado, solo me quedo con los elementos que coinciden con el tiempo
                # que tardo en infectarse la computadora
                pathsWeight[str(singlePath)] = nx.path_weight(miGrafo, singlePath, 'weight')

    return pathsWeight

def nodoCoincidente(miGrafoDijkstra):
    posiblesNodos = []
    for path, weight in miGrafoDijkstra.items():
        path = re.findall('\d+', path)
        for nodo in path:
            posiblesNodos.append(nodo)

    contadorCoincidencias = Counter(posiblesNodos)
    nodoCoincidencias = max(contadorCoincidencias, key=contadorCoincidencias.get)
    #Devuelve el nodo que se repite en todos los casos, por ende es el nodo en comun entre todos los tiempos dados.
    #No pude hacer que devuelva multiples nodos en caso de que halla multiples nodos que cumplan la condicion de ser el
    #posible caso '0'
    return nodoCoincidencias

def leerArchivo(archivo):
    with open(archivo, 'r') as f:
        fContenido = f.readlines()

    vertices = []
    aristas = []
    #Creo todos los vertices y Aristas
    for linea in fContenido[1:int(fContenido[0])]:
        # Elimino el sufijo \n de cada linea y luego creo una lista con cada valor de cada linea
        linea = linea.replace('\n', '')
        linea = linea.split(' ')

        # Creo los vertices y compruebo que no se repitan
        if linea[0] not in vertices:
            vertices.append(linea[0])
        if linea[2] not in vertices:
            vertices.append(linea[2])

        # Creo las aristas
        aristas.append([linea[0], linea[2], int(linea[1])])

    #Creo la lista de nodos infectados
    nodosInfectados = []
    for linea in fContenido[int(fContenido[0]) + 2: len(fContenido)]:
        linea = linea.replace('\n', '')
        linea = linea.split(' ')
        nodosInfectados.append([linea[0], int(linea[1])])

    return vertices, aristas, nodosInfectados

def escribirArchivo(resultado):
    with open('GusanoResultado.txt', 'w') as f: #el parametro w sobreescribe el archivo, si queremos modificarlo se usa 'e'
        f.write(resultado)

def Resolver(archivo):
    vertices, aristas, nodosInfectados = leerArchivo(archivo)
    miGrafo = crearGrafo(vertices, aristas)
    miGrafoDijkstra = nodoDijkstra(miGrafo, nodosInfectados)
    resultado = nodoCoincidente(miGrafoDijkstra)
    escribirArchivo(resultado)
    return resultado


print('Computadora donde se genero el Gusano: '+Resolver('Gusano1.txt'))