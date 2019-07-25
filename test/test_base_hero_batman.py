import unittest

from application.base_hero import BaseHero

class TestBaseHero(unittest.TestCase):

    def setUp(self):
        self.__robin = BaseHero("Damian", 1000)

    def test_base_hero_name(self):
        self.assertEqual(self.__robin.get_name(), "Damian")

    def test_base_hero_base_level(self):
        self.assertGreater(self.__robin.get_base_level(), 100)

if __name__ == '__main__':
    unittest.main()