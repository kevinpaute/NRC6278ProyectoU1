#Importamos libreria Queue
from queue import Queue
#Importamos emoji
import emoji 

#Clase Grafo
class Grafo:
    """
    Realizamos la creación de nuestra clase Grafo y agregamos los métodos y atributos que se requieren.
    
    ...

    Atributos
    ---------
        m_numero_nodos: int
            Número de nodos que tendrá el grafo.
        m_nodos: list
            Lista de nodos que tendrá el grafo.
        m_dirigido: bool
            Determina si el grafo es dirigido o no.
        m_direcciones: dict
            Diccionario de datos que contiene los nodos y sus direcciones.
        m_lista_adyacencia: dict
            Diccionario de datos que contiene los nodos y sus listas de adyacencia.
    Métodos
    -------
        __init__(self, num_nodos, restaurantes, dirigido=True):
            Constructor de la clase Grafo.
        agregar_arista(self, nodo1, nodo2, peso=1):
            Agrega una arista al grafo.
        imprimir_grafo(self):
            Imprime el grafo.
    """


    def __init__(self, num_nodos, restaurantes, dirigido=True):
        """
        Constructor de la clase Grafo.

        Parámetros
        ----------
            num_nodos: int
                Número de nodos que tendrá el grafo.
            restaurantes: list
                Lista de restaurantes que tendrá el grafo.
            dirigido: bool
                Determina si el grafo es dirigido o no.

        Retorna
        --------
            None

        """
        try:
            #Asignamos valores al número de nodos mediante el parámetro que se recibio 
            self.m_numero_nodos = num_nodos
            # Se genera el rango de nodos en base a m_numero_nodos
            self.m_nodos = range(self.m_numero_nodos)
            #Determinar que tipo de grafo es
            self.m_dirigido = dirigido
            #Creación del diccionario de datos con los nodos
            self.m_direcciones = restaurantes
            
            #En la lista de adyacencia se crea el diccionario de datos
            self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}
        except Exception as e:  
            print(e)
    

    def agregar_arista(self, nodo1, nodo2, peso=1):
        """
        Agrega una arista al grafo.

        Parámetros
        ----------
            nodo1: int
                Nodo inicial de la arista.
            nodo2: int
                Nodo final de la arista.
            peso: int
                Peso de la arista.
                
        Retorna
        --------
            None
        """
        try:
            # Agrega el nodo 2 a la lista de adyacencia del nodo 1
            self.m_lista_adyacencia[nodo1].add((nodo2, peso))
            if not self.m_dirigido:
                # Agrega el nodo 1 a la lista de adyacencia del nodo 2
                self.m_lista_adyacencia[nodo2].add((nodo1, peso))
        except Exception as e:
            print(e)


    def imprimir_grafo(self):
        """
        Imprime el grafo en formato JSON.

        Parámetros
        ----------
            None

        Retorna
        --------
            None
        """

        try:
            #recorre la lista de adyacencia
            for llave in self.m_lista_adyacencia.keys():
                #imprime la lista de adyacencia para cada nodo almacenado.
                print("Nodo", llave, ": ", self.m_lista_adyacencia[llave])

        #Si se produce un error se imprime en pantalla
        except Exception as e:
            print(e)


    def recorrido_dfs(self, nodo_inicio, nodo_objetivo, ruta = [], nodo_visitado = set()):
        """
        Recorrido en profundidad.

        Parámetros
        ----------
            nodo_inicio: int
                Nodo inicial del recorrido.
            nodo_objetivo: int
                Nodo final del recorrido.
            ruta: list
                Lista de nodos que forman la ruta.
            nodo_visitado: set
                Nodos que ya fueron visitados.

        Retorna
        --------
            ruta: list
                Lista de nodos que forman la ruta.

        """
        try:
            # Se agrega el nodo inicial a la lista de visitados
            nodo_visitado.add(nodo_inicio)
            # Se agrega el nodo inicial a la lista de ruta
            ruta.append(restaurantes[nodo_inicio])
        #Si se produce un error se imprime en pantalla
        except Exception as e:
            print(e)
        
        try:
            # Si el nodo inicial es el objetivo se imprime el recorrido
            if nodo_inicio == nodo_objetivo:
                print("Recorrido: ", ruta)
                return ruta

            # Se recorre la lista de adyacencia del nodo inicial
            for(vecino, peso) in self.m_lista_adyacencia[nodo_inicio]:
                # Si el nodo vecino no ha sido visitado se llama al metodo dfs con el nodo vecino como inicio
                if vecino not in nodo_visitado:
                    #se asigna a la variable resultado el nodo vecino, el objetivo, la ruta y la lista de nodos visitados
                    resultado = self.recorrido_dfs(vecino, nodo_objetivo, ruta, nodo_visitado) 
                    # Si el resultado no es nulo se retorna el resultado
                    if resultado is not None:
                        #Retorna resultado
                        return resultado 
        except Exception as e:
            print(e)

        try:
            # Si el resultado es nulo se retorna None        
            ruta.pop() 
            return None
        #Si se produce un error se imprime en pantalla
        except Exception as e:
            print(e)
