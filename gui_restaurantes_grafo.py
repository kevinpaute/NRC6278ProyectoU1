from interfaz_grafica import *
from PyQt5.QtWidgets import QTableWidgetItem
import sys

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



class Aplicacion(QMainWindow):
#Inicializar la interfaz grafica de la aplicacion y sus componentes a partir de gui.py
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.recorrido)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_salir.clicked.connect(self.salir)


    def recorrido(self):
        error = QMessageBox()
        #Ingresar n veces los nodos para el recorrido
        
        try:
            nodo_inicio = int(self.ui.line_nodo1.text())
            #Permitir que el usuario ingrese solamente el 3, 6,9,15,19,24
            if nodo_inicio in [3,6,9,15,19,24]:
                try:
                    nodo_objetivo = int(self.ui.line_nodo2.text())
                    #Si el nodo objetivo no esta entre 3,6,9,15,19,24
                    if nodo_objetivo not in [3,6,9,15,19,24] and nodo_objetivo >= 0 and nodo_objetivo< 26:
                        #Se llama al metodo recorrido_dfs para visualizar el recorrido
                        recorrido = grafo.recorrido_dfs(nodo_inicio, nodo_objetivo, [])
                        #Se inserta el recorrido en el text browser
                        self.ui.textBrowser.insertPlainText(str(recorrido))
                    #Si el nodo objetivo esta entre 3,6,9,15,19,24
                    else:
                        error.setText("Ingrese una opcion valida para el nodo objetivo")
                        error.exec_()
                        self.ui.line_nodo2.setText("")
                        self.ui.line_nodo2.setFocus() 

                    #Si se produce un error se imprime en pantalla
                except Exception as e:
                        error.setText("Ingrese una opcion valida")
                        #Se muestra el error en pantalla
                        error.exec_()
                        self.ui.line_nodo2.setText("")
                        return                   
            else:
                error.setText("Ingrese una opcion valida para el nodo inicial")
                error.exec_()
                self.ui.line_nodo1.setText("")
                return
        #Si se produce un error se imprime en pantalla
        except Exception as e:
            #Se muestra el error en pantalla
            error.setText("Ingrese una opcion valida")
            error.exec_()
            self.ui.line_nodo1.setText("")
            return


    def salir(self):
        """
        Salir de la aplicacion.
        
        Parámetros
        ----------
            None
            
        Retorna
        ----------
            None
        """
        #Salir de la aplicacion
        sys.exit()
        

    def limpiar(self):
        """
        Limpiar los campos de texto.
            
        Parámetros
        ----------
            None
                
        Retorna
        ----------
            None
        """
        #Limpiar los campos de texto
        self.ui.line_nodo1.clear()
        self.ui.line_nodo2.clear()
        self.ui.textBrowser.clear()


if __name__ == "__main__":

    #Dicionario de restaurantes
    restaurantes = {0:"McDonald's🍔",1:"Pizzeria El Hornero🍕",2:"Casa Bambú🍱",3:"CNT🏢",4:"Donde Coco🍛",5:"La Cocina de Consuelo🍚",
    6:"Universidad PUCE🏬",7:"Mandayan Chill & Fest🍲", 8:"Santo Moro Grill🦐", 9:"Universidad UTE🏬", 10:"Parrilladas Oh que rico🥓",
    11:"Mr. Pincho🥓", 12:"Margarita🍱", 13:"KFC🍗🍟", 14:"El Rincón del Che🍚", 15:"Universidad ESPE🏬", 16:"Conchal Chabelita🦐", 
    17:"El Menestron🍛", 18:"Pizza Hurt🍕", 19:"Municipio🏢",20:"La Cuchara Brava🍲",21:"Legends Food & Drinks 🍟",22:"Super Pollo🍗",
    23:"Papa John's Pizza🍟",24:"Supermercado AKI🏬", 25:"La Pizzeria🍕"}



    #Se instancia la clase Grafo con el diccionario de restaurantes y con dirigido en False
    grafo = Grafo(26, restaurantes, dirigido=False)

    #Se agregan las aristas al grafo
    grafo.agregar_arista(0, 1, 3)
    grafo.agregar_arista(0, 4, 7)
    grafo.agregar_arista(1, 3, 5)
    grafo.agregar_arista(3, 2, 1)
    grafo.agregar_arista(4, 5, 4)
    grafo.agregar_arista(2, 8, 7)
    grafo.agregar_arista(2, 6, 8)
    grafo.agregar_arista(5, 8, 6)
    grafo.agregar_arista(5, 10, 5)
    grafo.agregar_arista(8, 7, 3)
    grafo.agregar_arista(8, 9, 5)
    grafo.agregar_arista(7, 15, 3)
    grafo.agregar_arista(9, 10, 6)
    grafo.agregar_arista(9, 14, 4)
    grafo.agregar_arista(10, 12, 9)
    grafo.agregar_arista(12, 11, 5)
    grafo.agregar_arista(12, 18, 3)
    grafo.agregar_arista(15, 14, 5)
    grafo.agregar_arista(14, 13, 4)
    grafo.agregar_arista(18, 16, 2)
    grafo.agregar_arista(16, 13, 3)
    grafo.agregar_arista(13, 20, 10)
    grafo.agregar_arista(16, 17, 3)
    grafo.agregar_arista(17, 19, 7)
    grafo.agregar_arista(17, 22, 5)
    grafo.agregar_arista(20, 21, 6)
    grafo.agregar_arista(21, 19, 4)
    grafo.agregar_arista(22, 23, 7)
    grafo.agregar_arista(23, 21, 4)
    grafo.agregar_arista(23, 24, 8)
    grafo.agregar_arista(24, 25, 5)



    #Se llama al metodo imprimir_grafo para visualizar el grafo
    grafo.imprimir_grafo()

    #Se instancia la clase Aplicacion


    #Se crea una instancia de la clase QApplication 
    app = QApplication(sys.argv) 
    #Se crea una instancia de la clase Aplicacion
    window = Aplicacion()
    #Se muestra la ventana
    window.show()
    #Se ejecuta la aplicacion
    sys.exit(app.exec_())
    

