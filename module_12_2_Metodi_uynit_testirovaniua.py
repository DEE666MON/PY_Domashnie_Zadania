import unittest
from module_12_2 import *


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_wk = Runner("test_wk")
        for _ in range(10):
            test_wk.walk()
        self.assertEqual(test_wk.distance, 50)

    def test_run(self):
        test_rn = Runner("test_rn")
        for _ in range(10):
            test_rn.run()
        self.assertEqual(test_rn.distance, 100)


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.R1 = Runner("Усэйн", 10)
        self.R2 = Runner("Андрей", 9)
        self.R3 = Runner("Ник", 3)

    def test_tour1(self):
        finishers1 = Tournament(90, self.R1, self.R3).start()
        self.all_results[1] = finishers1
        self.assertTrue(finishers1[2] == "Ник")

    def test_tour2(self):
        finishers2 = Tournament(90, self.R2, self.R3).start()
        self.all_results[2] = finishers2
        self.assertTrue(finishers2[2] == "Ник")

    def test_tour3(self):
        finishers3 = Tournament(90, self.R1, self.R2, self.R3).start()
        self.all_results[3] = finishers3
        self.assertTrue(finishers3[3] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)


if __name__ == "__main__":
    unittest.main()
