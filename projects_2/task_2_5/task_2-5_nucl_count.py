dna = input("Введите последовательность ДНК: ").upper()
count_A = dna.count("A")
count_G = dna.count("G")
count_C = dna.count("C")
count_T = dna.count("T")

len_dna = len(dna)

pr_A = (count_A * 100) / len_dna
pr_G = (count_G * 100) / len_dna
pr_C = (count_C * 100) / len_dna
pr_T = (count_T * 100) / len_dna

print("=== Анализ последовательности ДНК ===")
print(f"Введите последовательность ДНК: {dna}")
print(f"\nПоследовательность в верхнем регистре: {dna.upper()}")
print("\nПодсчёт нуклеотидов:")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")
print(f"\nОбщая длина: {len_dna}")
print("\nПроцентное содержание нуклеотидов:")
print("A\tG\tC\tT")
print(f"{pr_A:.2f} %\t{pr_G:.2f} %\t{pr_C:.2f} %\t{pr_T:.2f} %")
