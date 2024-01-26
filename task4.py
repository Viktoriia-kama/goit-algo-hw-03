# Cтворіть функцію, яка допоможе вам визначати, кого з колег потрібно привітати у найближчі 7 днів

from datetime import datetime as dtdt
from datetime import timedelta

def get_upcoming_birthdays(users: list) -> list:
    # знаходимо поточну дату
    time_now = dtdt.today().date()

    new_list = []

    # перебираємо список по словниках
    for dictionary in users:
        birthday = dtdt.strptime(dictionary['birthday'], "%Y.%m.%d").date()  # перетворюємо рядок дати from dict на об'єкт datetime
        birthday = birthday.replace(year = time_now.year)             # змінюємо рік на 2024
        days = (birthday - time_now).days                             # рахуємо кількість днів до ДН
        
        if days <= 7:

            # встановлюємо дату привітання на ПН, якщо ДН у СБ або НД
            if birthday.weekday() == 5:
                birthday = birthday + timedelta(days = 2)             
            elif birthday.weekday() == 6:
                birthday = birthday + timedelta(days = 1)

            # створюємо кожного разу новий словник для нових значень
            current_dict = {}
            current_dict['name'] = dictionary['name']                                  # додаємо ім'я до словника
            current_dict['congratulation_date'] = dtdt.strftime(birthday, "%Y.%m.%d")  # додаємо дату привітання до словника
            new_list.append(current_dict)

    return new_list
            
users = [
    {"name": "sem", "birthday": "1985.01.28"},
    {"name": "katya", "birthday": "1985.01.27"},
    {"name": "vika", "birthday": "2005.02.23"},
    {"name": "vira", "birthday": "1990.01.31"}
]
result = get_upcoming_birthdays(users)
print("\nПРИВІТАЙ")
for dict in result:
    print(f'\n\t{dict['name']} \t{dict['congratulation_date']}')


