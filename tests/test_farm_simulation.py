import pytest
from farm.farm_simulation import Animal, Cow, Sheep, Chicken


#tests for Animal
@pytest.fixture
def animal() -> Animal:
    return Animal("Clarence", "AAAAAAAAAAAAA")
    

def test_animal_make_sound(animal: Animal, capsys):
    animal.make_sound()
    captured = capsys.readouterr()
    assert captured.out == "Animal Clarence says AAAAAAAAAAAAA\n"


def test__str__(animal):
    assert str(animal) == str(Animal("Clarence", "AAAAAAAAAAAAA"))


def test_feed(animal, capsys):
    animal.feed("meat")
    captured = capsys.readouterr()
    assert captured.out == "Clarence eats meat.\n"


@pytest.mark.parametrize("input", [1, 1.3, [], {1, 2, 3}, {}, ("",), None])
def test_feed_wrong_str(animal, input):
    with pytest.raises(TypeError):
        animal.feed(input)


#tests for Cow
@pytest.fixture
def cow() -> Cow:
    return Cow("Betty")


def test_cow_make_sound(cow, capsys):
    cow.make_sound()
    captured = capsys.readouterr()
    assert captured.out == "Cow Betty says Moo.\n"


def test_cow__str__(cow):
    assert str(cow) == str(Cow("Betty"))


@pytest.mark.parametrize("input", [1, 1.3, [], {1, 2, 3}, {}, ("",), None])
def test_cow_feed_with_wrong_input(cow, input):
    with pytest.raises(TypeError):
        cow.feed(input)


@pytest.fixture
def sheep() -> Sheep:
    return Sheep("Molly")


def test_sheep__str__(sheep):
    assert str(sheep) == str(Sheep("Molly"))


def test_sheep_make_sound(sheep, capsys):
    sheep.make_sound()
    captured = capsys.readouterr()
    assert captured.out == "Sheep Molly says Baa.\n"


@pytest.mark.parametrize("input", [1, 1.3, [], {1, 2, 3}, {}, ("",), None])
def test_sheep_feed_with_wrong_input(sheep, input):
    with pytest.raises(TypeError):
        sheep.feed(input)


@pytest.fixture
def chicken() -> Chicken:
    return Chicken("Smith")


def test_chicken__str__(chicken):
    assert str(chicken) == str(Chicken("Smith"))


def test_chicken_make_sound(chicken, capsys):
    chicken.make_sound()
    captured = capsys.readouterr()
    assert captured.out == "Chicken Smith says Bawk.\n"


def test_chicken_feed(chicken, capsys):
    chicken.feed("seeds")
    captured = capsys.readouterr()
    assert captured.out == "Chiken Smith eats seeds and laid an egg!\n"
