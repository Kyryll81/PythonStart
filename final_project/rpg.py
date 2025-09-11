class Character:
    def __init__(self, name, base_damage) -> None:
        self.name = name
        self._health = 100
        self._mana = 100
        self.base_damage = base_damage
    
    
    @property
    def health(self) -> int:
        return self._health
    
    
    @property
    def mana(self):
        return self._mana
    
    
    @health.setter
    def health(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError
        
        if value < 0:
            print("Forbidden to set negative values to health.")
            self._health = 0
            return
        
        self._health = value
    
    
    @mana.setter
    def mana(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError
        
        if value < 0:
            print("Forbidden to set negative values to mana.")
            self._mana = 0
            return
        
        self._mana = value


    def __str__(self) -> str:
        return f"Character({self.name}, {self._health}, {self._mana}, {self.base_damage})"
    
    
    def __eq__(self, other) -> bool:
        return self.name == other.name
    
    
    def attack(self, target: str) -> None:
        print(f"{self.name} is going to attack {target}!")


    @staticmethod
    def get_base_description() -> None:
        print("This is character in RPG world.")


class Knight(Character):
    def __init__(self, name, base_damage) -> None:
        super().__init__(name, base_damage)


    def attack(self, target: Character) -> None:
        target.health = target.health - self.base_damage
    
    
    def shield_block(self):
        print("Knight blocks attack.")
        self.health += 10


class Mage(Character):
    def __init__(self, name, base_damage) -> None:
        super().__init__(name, base_damage)
    
    def attack(self, target: Character) -> None:
        if self.mana >= 10:
            target.health = int(target.health - self.base_damage * 1.5)
            self.mana = self.mana - 10
            return
        print("Not enough mana!")