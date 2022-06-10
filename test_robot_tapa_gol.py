from robot_tapa_gol import robot_tapa_gol
import unittest

class TestRobotTapaGol(unittest.TestCase):
    def test_robot_tapa_gol(self):
        self.assertEqual(robot_tapa_gol(), True)

if __name__ == '__main__':
    unittest.main()