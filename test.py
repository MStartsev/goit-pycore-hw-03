from task_1 import get_days_from_today
from task_2 import get_numbers_ticket
from task_3 import normalize_phone
from task_4 import get_upcoming_birthdays


if __name__ == "__main__":
    print(get_numbers_ticket(1, 49, 6))
    print(get_days_from_today("2023-12-30"))

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
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

    users = [
        {"name": "John", "birthday": "1990.12.31"},  # завтра
        {"name": "Emma", "birthday": "1995.01.04"},  # через 3 дні
        {"name": "Alex", "birthday": "1987.02.05"},  # через 7 днів
        {"name": "Kate", "birthday": "1989.05.07"},  # через 8 днів
        {"name": "Mike", "birthday": "1993.12.29"},  # вчора
        {"name": "Tom", "birthday": "1985.12.30"},  # сьогодні
    ]

print(get_upcoming_birthdays(users))