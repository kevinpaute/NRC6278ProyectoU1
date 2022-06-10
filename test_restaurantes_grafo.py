# from restaurantes_grafo import Grafo
# import unittest

# #pruebas unittest 
# class TestGrafo(unittest.TestCase):
#     """
#     Clase para pruebas unitarias de la clase Grafo.
#     """
#     def test_grafo(self):
#         """
#         Prueba unitaria para la clase Grafo.
#         """
#         #Diccionario
#         restaurantes = {0:"McDonald's🍔",1:"Pizzeria El Hornero🍕",2:"Casa Bambú🍱",3:"CNT🏢",4:"Donde Coco🍛",5:"La Cocina de Consuelo🍚",
#         6:"Universidad PUCE🏬",7:"Mandayan Chill & Fest🍲", 8:"Santo Moro Grill🦐", 9:"Universidad UTE🏬", 10:"Parrilladas Oh que rico🥓",
#         11:"Mr. Pincho🥓", 12:"Margarita🍱", 13:"KFC🍗🍟", 14:"El Rincón del Che🍚", 15:"Universidad ESPE🏬", 16:"Conchal Chabelita🦐",
#         17:"El Menestron🍛", 18:"Pizza Hurt🍕", 19:"Municipio🏢",20:"La Cuchara Brava🍲",21:"Legends Food & Drinks 🍟",22:"Super Pollo🍗",
#         23:"Papa John's Pizza🍟",24:"Supermercado AKI🏬", 25:"La Pizzeria🍕"}

#         #Se instancia la clase Grafo con el diccionario de restaurantes y con dirigido en False
#         grafo = Grafo(26, restaurantes, dirigido=False)

#         #Se agregan las aristas al grafo
#         grafo.agregar_arista(0, 1, 3)
#         grafo.agregar_arista(0, 4, 7)
#         grafo.agregar_arista(1, 3, 5)
#         grafo.agregar_arista(3, 2, 1)
#         grafo.agregar_arista(4, 5, 4)
#         grafo.agregar_arista(2, 8, 7)
#         grafo.agregar_arista(2, 6, 8)
#         grafo.agregar_arista(5, 8, 6)
#         grafo.agregar_arista(5, 10, 5)
#         grafo.agregar_arista(8, 7, 3)
#         grafo.agregar_arista(8, 9, 5)
#         grafo.agregar_arista(7, 15, 3)
#         grafo.agregar_arista(9, 10, 6)
#         grafo.agregar_arista(9, 14, 4)
#         grafo.agregar_arista(10, 12, 9)
#         grafo.agregar_arista(12, 11, 5)
#         grafo.agregar_arista(12, 18, 3)
#         grafo.agregar_arista(15, 14, 5)
#         grafo.agregar_arista(14, 13, 4)
#         grafo.agregar_arista(18, 16, 2)
#         grafo.agregar_arista(16, 13, 3)
#         grafo.agregar_arista(13, 20, 10)
#         grafo.agregar_arista(16, 17, 3)
#         grafo.agregar_arista(17, 19, 7)
#         grafo.agregar_arista(17, 22, 5)
#         grafo.agregar_arista(20, 21, 6)
#         grafo.agregar_arista(21, 19, 4)
#         grafo.agregar_arista(22, 23, 7)
#         grafo.agregar_arista(23, 21, 4)
#         grafo.agregar_arista(23, 24, 8)
#         grafo.agregar_arista(24, 25, 5)

#         #Se llama al metodo imprimir_grafo para visualizar el grafo
#         grafo.imprimir_grafo()
        
#         #Se llama al metodo recorrido_dfs para visualizar el recorrido
#         print("\nRecorrido para llegar al restaurante 🍽️: ")
#         grafo.recorrido_dfs()

# if __name__ == '__main__':
#     unittest.main()