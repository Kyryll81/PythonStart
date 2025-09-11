from rpg import Mage, Knight


mage = Mage("Hornet", 10)
knight = Knight("Hollow", 20)

heroes: list = [knight, mage]

for i, hero in enumerate(heroes):
    heroes[i].attack(heroes[i-1])
    print(*heroes)
