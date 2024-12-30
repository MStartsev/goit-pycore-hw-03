from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Визначає список колег, яких потрібно привітати протягом наступного тижня.

    Args:
        users (list): Список словників з іменами та днями народження користувачів

    Returns:
        list: Список словників з іменами та датами привітань
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if days_until_birthday < 0 or days_until_birthday > 7:
            continue

        congratulation_date = birthday_this_year

        if congratulation_date.weekday() >= 5:  # Субота або неділя
            congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))

        upcoming_birthdays.append(
            {
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            }
        )

    return upcoming_birthdays
