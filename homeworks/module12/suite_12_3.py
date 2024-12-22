from unittest import TestSuite, TestLoader, TextTestRunner
import module_12_3

runnerST = TestSuite()
runnerST.addTest(TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest1))
runnerST.addTest(TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest2))
runnerST.addTest(TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest3))
runnerST.addTest(TestLoader().loadTestsFromTestCase(module_12_3.RunnerTest))


runner = TextTestRunner(verbosity=2)
runner.run(runnerST)