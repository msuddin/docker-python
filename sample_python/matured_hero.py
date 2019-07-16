from sample_python.base_hero import BaseHero


class MaturedHero(BaseHero):

    __power = ""

    def __init__(self, name, base_level, power):
        super(MaturedHero, self).__init__(name, base_level)
        self.__power = power

    def set_power(self, power):
        self.__power = power

    def get_power(self):
        return self.__power