# Створіть функцію, яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей



import random

def get_numbers_ticket(min, max, quantity):
    # перевіряємо чи параметри функції є правильними
    if min < 1 or max > 1000 or quantity > max - min:
        return  []
    
    list = []
    # створюємо цикл, який генерує випадкові унікальні числа, поки не набереться quantity штук
    while len(list) < quantity:
        a = random.randint(min, max)
        if a not in list:
            list.append(a)

    # сортуємо випадкові числа
    list.sort()
    return list

min = int(input("Введіть мінімальне можливе число у наборі: "))
max = int(input("Введіть максимальне можливе число у наборі: "))
quantity = int(input("Введіть кількість чисел, які потрібно вибрати: "))

lottery_numbers = get_numbers_ticket(min, max, quantity)
print(f"Ваші лотерейні числа:{lottery_numbers}")