from datetime import datetime


def get_days_from_today(date):
    """
    Розраховує кількість днів між заданою датою та поточною датою.

    Args:
        date (str): Дата у форматі 'РРРР-ММ-ДД'

    Returns:
        int: Кількість днів між датами
    """
    try:
        # Перетворення рядка в об'єкт datetime
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Отримання поточної дати
        current_date = datetime.today().date()
        # Розрахунок різниці в днях
        difference = (current_date - input_date).days
        return difference
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'")
