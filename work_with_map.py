# Перетворення рядків у числа

str_numbers: list[str] = ["10", "25", "50", "15"]
print(list(map(int, str_numbers)))

# Обробка цін
prices: list = [100, 250, 75, 420]
print(list(map(lambda x: x - 0.2 * x, prices)))


# Об'єднання імен
first_names: list[str] = ["Іван", "Марія", "Олександр"]
last_names: list[str] = ["Петров", "Іванова", "Коваль"]
print(list(map(lambda a, b: a + " " + b, first_names, last_names)))

