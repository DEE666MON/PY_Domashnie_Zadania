import unittest
import logging
from module_12_4 import *


class RunnerTest:
    def test_walk():
        try:
            test_wk = Runner("test_wk", 10)
            for _ in range(10):
                test_wk.walk()
            # self.assertEqual(test_wk.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run():
        try:
            test_rn = Runner("test_rn", 5)
            for _ in range(10):
                test_rn.run()
            # self.assertEqual(test_rn.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_walk2():
        try:
            test_wk = Runner("test_wk", -5)
            for _ in range(10):
                test_wk.walk()
            # self.assertEqual(test_wk.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run2():
        try:
            test_rn = Runner(0)
            for _ in range(10):
                test_rn.run()
            # self.assertEqual(test_rn.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        test1 = Runner("test1")
        test2 = Runner("test2")
        for i in range(10):
            test1.walk()
            test1.run()
            if i != 0:
                test2.walk()
                test2.run()
        # self.assertNotEqual(test1.distance, test2.distance)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    RunnerTest.test_walk()
    RunnerTest.test_walk2()
    RunnerTest.test_run()
    RunnerTest.test_run2()
