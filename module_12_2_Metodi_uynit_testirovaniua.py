import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
        return finishers


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
