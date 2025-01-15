from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
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
