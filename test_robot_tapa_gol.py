from robot_tapa_gol import robot_tapa_gol
import unittest

class TestRobotTapaGol(unittest.TestCase):
    # Test para validar que el robot se mueva correctamente
    def test_robot_tapa_gol(self): 
        # Si el robot_tapa_gol() retorna True, el test pasa
        self.assertEqual(robot_tapa_gol(), True) 

if __name__ == '__main__':
     # Se ejecuta el test
    unittest.main()