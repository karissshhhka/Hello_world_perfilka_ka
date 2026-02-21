reagent_name = input()
amount_of_reagent = int(input())
print(f"Реактив {reagent_name} поступил на склад в количестве {amount_of_reagent} шт.")

f = open(r"C:\Users\Karisha\Desktop\perfilka_ka\projects_2\inventory.txt", "w", encoding="utf-8")
print(f"Реактив {reagent_name} поступил на склад в количестве {amount_of_reagent} шт.", file=f)
f.close()