from farm_simulation import Cow, Sheep, Chicken


animals: list = [Cow("Cow 1"), Sheep("Sheep 1"), Chicken("Robochiken")]

for animal in animals:
    animal.make_sound()
    animal.feed("food")