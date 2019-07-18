class BaseHero(object):

    __name = ""
    __base_level = 0

    def __init__(self, name, base_level):
        self.__name = name
        self.__base_level = base_level

    def set_name(self, name):
        self.__name = name

    def set_base_level(self, age):
        self.__base_level = age

    def get_name(self):
        return self.__name

    def get_base_level(self):
        return self.__base_level

    def describe_hero(self):
        return "The name's {} and my base power is {} ".format(self.__name, self.__base_level)