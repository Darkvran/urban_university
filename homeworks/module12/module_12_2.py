from unittest import TestCase, main
from runner_and_tournament import Runner, Tournament


class TournamentTest1(TestCase):

    def setUp(self):
        self.runners = [Runner("Усэйн", 10), Runner("Ник", 3)]

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    def test_Tournament(self):
        tournament = Tournament(90, *self.runners)
        this_result = tournament.start()

        for i in range(len(self.runners)):
            this_result[i+1] = this_result[i+1].name

        self.all_results.append(this_result)
        self.assertTrue(this_result[len(self.runners)] == "Ник")

class TournamentTest2(TestCase):

    def setUp(self):
        self.runners = [Runner("Андрей", 9), Runner("Ник", 3)]

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    def test_Tournament(self):
        tournament = Tournament(90, *self.runners)
        this_result = tournament.start()

        for i in range(len(self.runners)):
            this_result[i+1] = this_result[i+1].name

        self.all_results.append(this_result)
        self.assertTrue(this_result[len(self.runners)] == "Ник")

class TournamentTest3(TestCase):

    def setUp(self):
        self.runners = [Runner("Усэйн", 10), Runner("Андрей", 9), Runner("Ник", 3)]

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    def test_Tournament(self):
        tournament = Tournament(90, *self.runners)
        this_result = tournament.start()

        for i in range(len(self.runners)):
            this_result[i+1] = this_result[i+1].name

        self.all_results.append(this_result)
        self.assertTrue(this_result[len(self.runners)] == "Ник")

if __name__ == "__main__":
    main()