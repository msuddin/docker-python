from application.base_hero import BaseHero
from application.matured_hero import MaturedHero

robin = BaseHero("Damian Wayne", 1500)
print(robin.describe_hero())

batman = MaturedHero("Bruce Wayne", 3500, "Fear Factor")
print(batman.describe_hero())

if robin.get_base_level() < 2000:
    print(robin.get_name() + " is not strong enough")