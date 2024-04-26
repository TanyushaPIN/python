# Программа проверки привышения скорости 
print("Введите скорость автомобиля: ", end = '')
speed = int(input())
if speed < 60 and speed > 0:
    print("норм")
elif speed <= 0:
    print("нуль")
elif speed == 60:
    print("тютелька в тютельку")
else:
    print("нарушил")