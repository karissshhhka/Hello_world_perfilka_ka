#!bin/bash
if [ $# -ge 2]; then
	name_gen="$1"
	expression_level="$2"
else
	echo "Недостаточно аргументов"
	read -p ("Введите имя гена: ") name_gen
	read -p ("Введите уровень экспрессии гена: ") expression_level
fi

echo "Экспрессия гена $name_gen составляет $expression_level единиц"

