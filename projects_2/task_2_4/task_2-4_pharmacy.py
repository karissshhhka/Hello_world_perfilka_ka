num_capsules = int(input("Введите общее количество произведенных капсул: "))
num_pack = int(input("Введите количество капсул в одной упаковке: "))

full_pack = num_capsules // num_pack
rem_capsuls = num_capsules % num_pack

print(f"--- Отчет фасовочного цеха ---\nПолных упаковок:\t{full_pack}\nОстаток капсул:\t\t{rem_capsuls}")