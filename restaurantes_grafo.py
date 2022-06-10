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
        _init_(self, num_nodos, restaurantes, dirigido=True):
            Constructor de la clase Grafo.
        agregar_arista(self, nodo1, nodo2, peso=1):
            Agrega una arista al grafo.
        imprimir_grafo(self):
            Imprime el grafo.
    """


    def _init_(self, num_nodos, restaurantes, dirigido=True):
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