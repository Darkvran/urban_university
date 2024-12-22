import unittest

from runner_and_tournament import Runner, Tournament
from unittest import TestCase


class TournamentTest1(TestCase):
    isFrozen = True
    def setUp(self):
        self.runners = [Runner("Усэйн", 10), Runner("Ник", 3)]

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    @unittest.skipIf(not isFrozen, "Не придумал причину")
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

class RunnerTest(TestCase):
    isFrozen = False

    @unittest.skipIf(not isFrozen, "Бегун должен бегать, а не ходить!)")
    def test_walk(self):
        runner = Runner('')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("1")
        runner2 = Runner("2")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)