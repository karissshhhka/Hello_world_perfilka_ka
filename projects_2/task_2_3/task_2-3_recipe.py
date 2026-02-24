name_of_enviroment = input("Введите название питательной среды: ")
concentration_agara = input("Введите концентрацию агара (%): ")
tempreture = input("Введите температуру стерилизации (°C): ")


with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{name_of_enviroment}\n\n| Параметры:\n")
    file.write(f"- Концентрация агара: {concentration_agara}%\n")
    file.write(f"- Температура стерилизации: {tempreture}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")