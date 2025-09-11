class Animal:
    def __init__(self, name: str, sound: str) -> None:
        self._name = name
        self._sound = sound
    
    
    def make_sound(self) -> None:
        print(f"Animal {self._name} says {self._sound}.")


    def feed(self, food: str) -> None:
        if not isinstance(food, str):
            raise TypeError("Wrong input data.")
        
        print(f"{self._name} eats {food}.")


    def __str__(self) -> str:
        return f"It is {self._name} says {self._sound}."


class Cow(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Moo")
    
    
    def make_sound(self) -> None:
        print(f"Cow {self._name} says {self._sound}.")


class Sheep(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Baa")
    
    
    def make_sound(self) -> None:
        print(f"Sheep {self._name} says {self._sound}.")


class Chicken(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Bawk")
    
    
    def make_sound(self) -> None:
        print(f"Chicken {self._name} says {self._sound}.")
    
    
    def feed(self, food: str) -> None:
        print(f"Chiken {self._name} eats {food} and laid an egg!")
