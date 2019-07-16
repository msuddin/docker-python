from sample_python.matured_hero import MaturedHero

name = "bruce"
base_level = 2500
power = "Fear Factor"

batman = MaturedHero(name, base_level, power)

def test_matured_hero_name():
    assert batman.get_name() == name

def test_matured_hero_base_level():
    assert batman.get_base_level() == base_level

def test_matured_hero_power():
    assert batman.get_power() == 1000
