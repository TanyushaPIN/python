#Программа расчета скорости

print("Введите время (в часах) и расстояние(в км)")
print("Time - ", end='')
time = float (input())
print("Sped - ", end='')
distance = float (input())

speed = distance/time

print("Скорость объекта составляет: ", speed)