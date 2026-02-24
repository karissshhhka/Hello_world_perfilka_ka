volume = int(input("Введите объем раствора (в мл): "))
mass_salt = volume * 0.009

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЁТ ПО ПРИГОТОВЛЕНИЮ:\n-----------------------\nОбщий обём:\t[{volume}] мл\nМасса соли:\t[{mass_salt:.2f}] г\nОбъём воды:\t[{volume}] мл")

