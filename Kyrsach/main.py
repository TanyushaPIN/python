import tkinter as tk

# Создаем окно
root = tk.Tk()
root.title("Калькулятор стоимости бензина")
root.configure(bg='black')

# Функция для подсчета итоговой цены
def calculate_price():
    liters = float(entry_liters.get())
    price_per_liter = 0
    if var.get() == 1:
        price_per_liter = 45  # Цена за литр бензина марки A
    elif var.get() == 2:
        price_per_liter = 50  # Цена за литр бензина марки B
    elif var.get() == 3:
        price_per_liter = 55  # Цена за литр бензина марки C
    
    discount = 0
    if card_var.get() == 1:
        discount = 0.05  # Обычная скидка 5%
    elif card_var.get() == 2:
        discount = 0.1  # Золотая скидка 10%
    elif card_var.get() == 3:
        discount = 0.15  # Платиновая скидка 15%
    
    total_price = liters * price_per_liter * (1 - discount)
    label_result.config(text="Итоговая цена: {:.2f} руб.".format(total_price))

# Создаем виджеты
label_liters = tk.Label(root, text="Введите количество литров бензина:", bg='black', fg='white')
label_liters.pack()
entry_liters = tk.Entry(root)
entry_liters.pack()

label_mark = tk.Label(root, text="Выберите марку бензина:", bg='black', fg='white')
label_mark.pack()
var = tk.IntVar()
tk.Radiobutton(root, text="A - 45 руб./л", variable=var, value=1, bg='black', fg='white').pack()
tk.Radiobutton(root, text="B - 50 руб./л", variable=var, value=2, bg='black', fg='white').pack()
tk.Radiobutton(root, text="C - 55 руб./л", variable=var, value=3, bg='black', fg='white').pack()

label_card = tk.Label(root, text="Выберите вашу скидочную карту:", bg='black', fg='white')
label_card.pack()
card_var = tk.IntVar()
tk.Radiobutton(root, text="Обычная - 5% скидка", variable=card_var, value=1, bg='black', fg='white').pack()
tk.Radiobutton(root, text="Золотая - 10% скидка", variable=card_var, value=2, bg='black', fg='white').pack()
tk.Radiobutton(root, text="Платиновая - 15% скидка", variable=card_var, value=3, bg='black', fg='white').pack()

btn_calculate = tk.Button(root, text="Рассчитать", command=calculate_price)
btn_calculate.pack()

label_result = tk.Label(root, text="", bg='black', fg='white')
label_result.pack()

root.mainloop()