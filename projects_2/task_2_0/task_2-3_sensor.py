name_operator = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"Оператор\tЗначение\n{name_operator}\t\t{pressure_value}")

print("Данные успешно сохранены в sensor_log.txt")