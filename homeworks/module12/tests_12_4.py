import logging
from rt_with_exceptions import Tournament, Runner
from unittest import TestCase

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner test.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(TestCase):
    def test_walk(self):
        try:
            runner = Runner('1', speed=-100)
            for _ in range(10):
                runner.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(runner.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(34534)
            for _ in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        runner1 = Runner("1")
        runner2 = Runner("2")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)