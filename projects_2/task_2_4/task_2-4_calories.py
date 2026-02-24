mass_prot = float(input("Введите массу белков в продукте (г): "))
mass_fats = float(input("Введите массу жиров в продукте (г): "))
mass_carb = float(input("Введите массу углеводов в продукте (г): "))

Kcal = mass_prot * 4 + mass_fats * 9 + mass_carb * 4
print(f"Килокалории составили: {Kcal}")