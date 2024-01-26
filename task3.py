# Розробіть функцію, що нормалізує телефонні номери до стандартного формату (залишаючи тільки цифри та символ '+' на початку)
import re

def normalize_phone(phone_number:str) -> str:
    pattern = r"[;,\-:!\. ()/\\t\\n]"                              # вказуємо, які символи потрібно видалити (усі спец. символи)
    replacement = "" 
    formatted_ph_num = re.sub(pattern, replacement, phone_number)  # видаляємо зайві символи

    # перевіряємо чи номер має код "38" та "+"
    pattern2 = '38'
    pattern3 = '+'
    if pattern2 not in phone_number:
        formatted_ph_num = pattern2 + formatted_ph_num
    if pattern3 not in phone_number:
        formatted_ph_num = pattern3 + formatted_ph_num
    
    return formatted_ph_num

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
column_width = 25
print(f"{'Оригінальні номери':<{column_width}}{'Нормалізовані номери'}")

# проходимось по обидвох списках і виводимо оригінальний номер та нормалізований
for i, j in zip(raw_numbers,sanitized_numbers):
    print(f"{i:<{column_width+3}}{j}")