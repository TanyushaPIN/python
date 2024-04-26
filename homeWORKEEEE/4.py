rubles = float(input("Введите сумму в рублях: "))
currency = input("Введите валюту (доллары, евро или юани): ")

if currency == "D":
    rate = 92.6  # Курс доллара
    converted_amount = rubles / rate
elif currency == "E":
    rate = 100.2  # Курс евро
    converted_amount = rubles / rate
elif currency == "U":
    rate = 12.7  # Курс юаня
    converted_amount = rubles / rate
else:
    print("Выбрана недопустимая валюта")
    converted_amount = None

# Вывод результата
if converted_amount is not None:
    print("Вы получите", round(converted_amount, 2), currency)