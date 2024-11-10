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
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    def setUp(self):
        self.R1 = Runner("Усэйн", 10)
        self.R2 = Runner("Андрей", 9)
        self.R3 = Runner("Ник", 3)
        self.assertTrue(expr=self.all_results[1][2].name == "Ник" and self.all_results[2][
            2].name == "Ник" and self.all_results[3][3].name == "Ник")

    def Tour1(self):
        T1 = Tournament(90, self.R1, self.R3).start()
        self.R1.distance = 0
        self.R3.distance = 0
        self.all_results[1] = T1

    def Tour2(self):
        T2 = Tournament(90, self.R2, self.R3).start()
        self.R2.distance = 0
        self.R3.distance = 0
        self.all_results[2] = T2

    def Tour3(self):
        T3 = Tournament(90, self.R1, self.R2, self.R3).start()
        self.all_results[3] = T3


if __name__ == "__main__":
    unittest.main()
