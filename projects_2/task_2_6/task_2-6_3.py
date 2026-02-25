donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите группу крови реципиента (I, II, III, IV): ").strip().upper()

if donor == recipient or donor == "I":
    print("Возможно переливание")
else:
    print("Переливание невохможно")