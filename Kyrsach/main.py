import tkinter as tk
from tkinter import simpledialog

# Функция для расчета цены
def calculate_price():
    try:
        # Получаем количество литров и проверяем, что это число
        liters = float(liters_entry.get())
        # Получаем выбранную марку бензина и скидку
        selected_fuel = fuel_var.get().split(':')[0]  # Извлекаем название марки
        selected_discount = discount_var.get()
        # Рассчитываем итоговую цену
        price = liters * fuel_prices[selected_fuel] * (1 - discounts[selected_discount] / 100)
        # Выводим цену
        result_label.config(text=f"Итоговая цена: {price:.2f} руб.")
    except ValueError:
        result_label.config(text="Пожалуйста, введите корректное число литров.")

# Функция для добавления новой марки бензина
def add_fuel():
    new_fuel = simpledialog.askstring("Добавить марку бензина", "Введите название марки:")
    new_price = simpledialog.askfloat("Добавить марку бензина", "Введите цену за литр:")
    if new_fuel and new_price:
        if (new_fuel not in fuel_prices) or (new_fuel in fuel_prices and fuel_prices[new_fuel] != new_price):
            fuel_prices[new_fuel] = new_price
            update_fuel_menu()  # Обновляем меню после добавления новой марки
        else:
            result_label.config(text= "Такая марка уже существует!")

# Функция для обновления меню марок бензина
def update_fuel_menu():
    menu = fuel_option_menu["menu"]
    menu.delete(0, "end")
    for fuel, price in fuel_prices.items():
        menu.add_command(label=f"{fuel}: {price} руб.", command=lambda value=fuel: fuel_var.set(f"{value}: {price} руб."))

# Функция для добавления новой скидки
def add_discount():
    new_discount = simpledialog.askinteger("Добавить скидку", "Введите процент скидки:")
    if new_discount is not None and f"{new_discount}%" not in discounts:
        discounts[f"{new_discount}%"] = new_discount
        discount_option_menu['menu'].add_command(label=f"{new_discount}%", command=tk._setit(discount_var, f"{new_discount}%"))
    else:
        result_label.config(text= "Такая скидка уже существует!")
# Начальные данные
fuel_prices = {'АИ-92': 40.0, 'АИ-95': 45.0, 'АИ-98': 50.0}
discounts = {'0%': 0, '5%': 5, '10%': 10}

# Создаем главное окно
root = tk.Tk()
root.title("Расчет стоимости бензина")
root.geometry("430x700")  # Увеличиваем размер окна

# Поля ввода и выбора
liters_label = tk.Label(root, text="Количество литров:", font=('Arial', 14))
liters_label.pack(pady=10)

liters_entry = tk.Entry(root, font=('Arial', 14), width=20)
liters_entry.pack(pady=10)

fuel_var = tk.StringVar(root)
fuel_var.set('АИ-92: 40 руб.')  # Устанавливаем начальное значение с ценой
fuel_option_menu = tk.OptionMenu(root, fuel_var, '')
fuel_option_menu.config(width=20, height=2, font=('Arial', 14))
fuel_option_menu.pack(pady=20)
update_fuel_menu()  # Вызываем функцию для инициализации меню

discount_var = tk.StringVar(root)
discount_var.set('0%')
discount_option_menu = tk.OptionMenu(root, discount_var, *discounts.keys())
discount_option_menu.config(width=20, height=2, font=('Arial', 14))
discount_option_menu.pack(pady=20)

# Кнопки
calculate_button = tk.Button(root, text="Рассчитать", command=calculate_price, font=('Arial', 14), width=20, height=2)
calculate_button.pack(pady=20)

add_fuel_button = tk.Button(root, text="Добавить марку бензина", command=add_fuel, font=('Arial', 14), width=20, height=2)
add_fuel_button.pack(pady=20)

add_discount_button = tk.Button(root, text="Добавить скидку", command=add_discount, font=('Arial', 14), width=20, height=2)
add_discount_button.pack(pady=20)

# Метка для вывода результата
result_label = tk.Label(root, text="Итоговая цена: ", font=('Arial', 14))
result_label.pack(pady=20)

# Запускаем главный цикл
root.mainloop()