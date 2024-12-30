from random import sample


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Генерує відсортований список унікальних випадкових чисел.

    Args:
        min (int): Мінімальне число (≥1)
        max (int): Максимальне число (≤1000)
        quantity (int): Кількість чисел

    Returns:
        list: Відсортований список унікальних чисел
    """
    if not (1 <= min <= max <= 1000 and min <= quantity <= max):
        return []

    return sorted(sample(range(min, max + 1), quantity))
