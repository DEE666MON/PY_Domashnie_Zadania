import unittest
import module_12_2_Metodi_uynit_testirovaniua

testSuite = unittest.TestSuite()
testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2_Metodi_uynit_testirovaniua.RunnerTest))
testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2_Metodi_uynit_testirovaniua.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testSuite)