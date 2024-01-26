# Створіть функцію, яка розраховує кількість днів між заданою датою і поточною датою

from datetime import datetime as dtdt

def get_days_from_today(date: str) -> int:
    time_now = dtdt.today().date()                 # отримуємо поточну дату
    date = dtdt.strptime(date, "%Y-%m-%d").date()  # перетворюємо отриманий у функцію рядок у datetime об'єкт
    days = (date - time_now).days                  # обчислюємо кількість днів до вказаної дати
    return (f"Кількість днів до {date} становить {days}")

# створюємо цикл для перевірки правильності введеня рядка з датою
while True:   
    try:
        date_x= input("Введіть дату, кількість днів до якої вас цікавить, у форматі YYYY-MM-DD ")
        date_x = dtdt.strptime(date_x, "%Y-%m-%d")
        date_x = date_x.strftime("%Y-%m-%d")
        break    
    except Exception as e:
        print("\nError! Будь ласка, введіть дату у форматі YYYY-MM-DD, наприклад 2020-01-22!")

print(get_days_from_today(date_x))
