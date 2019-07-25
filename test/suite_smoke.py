import unittest

from test import test_base_hero_robin, test_base_hero_batman

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_base_hero_robin))
suite.addTests(loader.loadTestsFromModule(test_base_hero_batman))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)