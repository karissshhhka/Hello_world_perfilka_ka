print("Стоит камень, а на нём три направления: налево, направо и прямо\nКуда пойдёшь?")
choice = input().strip().lower()
if choice == 1 or choice == "налево":
    print("Коня потерял")
elif choice == 2 or choice == "направо":
    print("Жизнь потерял")
elif choice == 3 or choice == "прямо":
    print("Щстался жив")
else:
    print("Остался у камня стоять навсегда")