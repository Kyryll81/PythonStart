import pytest
from unittest.mock import Mock

from rpg import Character, Knight, Mage


@pytest.fixture
def character() -> Character:
    return Character("Clarence", 10)


def test_set_health(character, capsys):
    character.health = -100
    captured = capsys.readouterr()
    assert captured.out == "Forbidden to set negative values to health.\n"


def test_set_mana(character, capsys):
    character.mana = -100
    captured = capsys.readouterr()
    assert captured.out == "Forbidden to set negative values to mana.\n"


def test__eq__(character):
    assert character == Character("Clarence", 10)


def test_get_base_description(capsys):
    Character.get_base_description()
    captured = capsys.readouterr()
    assert captured.out == "This is character in RPG world.\n"


@pytest.fixture
def knight() -> Knight:
    return Knight("Hollow", 20)


def test_knight_attack(knight, character):# probably would be better to mock character, but instead I can reuse fixture
    character.health = 100
    knight.attack(character)
    assert character.health == 80


@pytest.fixture
def mage() -> Mage:
    return Mage("Hornet", 10)


def test_mage_attack(mage, character):
    character.health = 100
    mage.mana = 100
    mage.attack(character)
    assert character.health == 100 - int(mage.base_damage * 1.5)
    assert mage.mana == 90


def test_mage_not_enough_mana(mage, character, capsys):
    character.health = 100
    mage.mana = 0
    mage.attack(character)
    captured = capsys.readouterr()
    assert captured.out == "Not enough mana!\n"
