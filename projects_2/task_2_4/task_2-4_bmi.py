weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

bmi = weight / (height ** 2)
print(f"--- Отчёт о состоянии здоровья\n Рост:\t\t {height} м.\n Вес:\t\t {weight} кг.\nИндекс массы тела пациента: {bmi:.2f}")