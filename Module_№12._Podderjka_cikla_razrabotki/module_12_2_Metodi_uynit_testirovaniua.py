import unittest
from module_12_2 import *


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        test_wk = Runner("test_wk")
        for _ in range(10):
            test_wk.walk()
        self.assertEqual(test_wk.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        test_rn = Runner("test_rn")
        for _ in range(10):
            test_rn.run()
        self.assertEqual(test_rn.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        test1 = Runner("test1")
        test2 = Runner("test2")
        for i in range(10):
            test1.walk()
            test1.run()
            if i != 0:
                test2.walk()
                test2.run()
        self.assertNotEqual(test1.distance, test2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.R1 = Runner("Усэйн", 10)
        self.R2 = Runner("Андрей", 9)
        self.R3 = Runner("Ник", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tour1(self):
        finishers1 = Tournament(90, self.R1, self.R3).start()
        self.all_results[1] = finishers1
        self.assertTrue(finishers1[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tour2(self):
        finishers2 = Tournament(90, self.R2, self.R3).start()
        self.all_results[2] = finishers2
        self.assertTrue(finishers2[2] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
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
