class Car:
    def __init__(self, made: str, model: str, year: str, engine_volume: float, fuel_efficiency: int) -> None:
        self.made = made
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.fuel_efficiency = fuel_efficiency
    
    
    def __str__(self) -> str:
        return f"Автомобіль: {self.year} {self.made} {self.fuel_efficiency}."
    
    
    def __repr__(self) -> str:
        return f'Car(made="{self.made}", model="{self.model}", year="{self.year}", engine_volume={self.engine_volume}, fuel_efficiency={self.fuel_efficiency})'
    
    
    def __eq__(self, other) -> bool:
        return self.made == other.made and self.model == other.model


    def calculate_fuel_consumption(self, distance_km: int) -> float:
        return self.fuel_efficiency / 100 * distance_km
    
    
    def shift_gear(self, gear: str | int) -> str:
        return f'Перемикаємо передачу на: {gear}'


if __name__ == "__main__":
    car1: Car = Car(made="Mazda", model="MC5", year="1916", engine_volume=95.5, fuel_efficiency=30)
    car2: Car = Car(made="Mazda", model="MC5", year="1916", engine_volume=95.5, fuel_efficiency=30)
    print(car1 == car2)
    print(car1)
    print(repr(car1))