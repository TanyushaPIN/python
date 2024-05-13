import tkinter as tk
root = tk.Tk()
root.title("Калькулятор стоимости бензина")
root.configure(bg='light grey')
root.geometry("400x400")

def calculate_price():
    liters = float(entry_liters.get())
    price_per_liter = 0
    if var.get() == 1:
        price_per_liter = 53.59   # Цена за литр бензина марки Аи-92
    elif var.get() == 2:
        price_per_liter = 59.89   # Цена за литр бензина марки Аи-95
    elif var.get() == 3:
        price_per_liter = 63.92   # Цена за литр бензина марки ДТ

    discount = 0
    if card_var.get() == 1:
        discount = 0.05  # Обычная скидка 5%
    elif card_var.get() == 2:
        discount = 0.1  # Золотая скидка 10%
    elif card_var.get() == 3:
        discount = 0.15  # Платиновая скидка 15%

    total_price = liters * price_per_liter * (1 - discount)
    label_result.config(text="Итоговая цена: {:.2f} руб.".format(total_price))

label_liters = tk.Label(root, text="Введите количество литров бензина:", bg='light grey', fg='black', font=("Arial", 12))
label_liters.pack()
entry_liters = tk.Entry(root, font=("Arial", 12))
entry_liters.pack()
label_mark = tk.Label(root, text="Выберите марку бензина:", bg='light grey', fg='black', font=("Arial", 12))
label_mark.pack()
var = tk.IntVar()
tk.Radiobutton(root, text="Аи-92 - 53.59 руб./л", variable=var, value=1, bg='light grey', fg='black', font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Аи-95 - 59.89 руб./л", variable=var, value=2, bg='light grey', fg='black', font=("Arial", 12)).pack()
tk.Radiobutton(root, text="ДТ - 63.92 руб./л", variable=var, value=3, bg='light grey', fg='black', font=("Arial", 12)).pack()
label_card = tk.Label(root, text="Выберите вашу скидочную карту:", bg='light grey', fg='black', font=("Arial", 12))
label_card.pack()
card_var = tk.IntVar()
tk.Radiobutton(root, text="Обычная - 5% скидка", variable=card_var, value=1, bg='light grey', fg='black', font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Золотая - 10% скидка", variable=card_var, value=2, bg='light grey', fg='black', font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Платиновая - 15% скидка", variable=card_var, value=3, bg='light grey', fg='black', font=("Arial", 12)).pack()
btn_calculate = tk.Button(root, text="Рассчитать", command=calculate_price, bg='grey', fg='white', font=("Arial", 12))
btn_calculate.pack()
label_result = tk.Label(root, text="", bg='light grey', fg='black', font=("Arial", 12))
label_result.pack()

def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()

btn_clear = tk.Button(root, text="Изменить данные", command=lambda: [clear_window(root), init_window()], bg='grey', fg='white', font=("Arial", 12))
btn_clear.pack()

def init_window():
    label_liters = tk.Label(root, text="Введите количество литров бензина:", bg='light grey', fg='black', font=("Arial", 12))
    label_liters.pack()
    entry_liters = tk.Entry(root, font=("Arial", 12))
    entry_liters.pack()
    label_price = tk.Label(root, text="Введите цену за литр бензина:", bg='light grey', fg='black', font=("Arial", 12))
    label_price.pack()
    entry_price = tk.Entry(root, font=("Arial", 12))
    entry_price.pack()
    label_discount = tk.Label(root, text="Введите скидку по карте (в процентах):", bg='light grey', fg='black', font=("Arial", 12))
    label_discount.pack()
    entry_discount = tk.Entry(root, font=("Arial", 12))
    entry_discount.pack()
    btn_calculate = tk.Button(root, text="Рассчитать", command=calculate_price, bg='grey', fg='white', font=("Arial", 12))
    btn_calculate.pack()
    label_result = tk.Label(root, text="", bg='light grey', fg='black', font=("Arial", 12))
    label_result.pack()

# Измените функцию calculate_price, чтобы она использовала новые входные данные
def calculate_price():
    liters = float(entry_liters.get())
    price_per_liter = float(entry_price.get())
    discount = float(entry_discount.get())
    total_price = liters * price_per_liter * (1 - discount)
    label_result.config(text="Итоговая цена: {:.2f} руб.".format(total_price))
root.mainloop()