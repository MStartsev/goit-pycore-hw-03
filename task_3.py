import re


def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонний номер до формату +380XXXXXXXXX.

    Args:
        phone_number (str): Телефонний номер у довільному форматі

    Returns:
        str: Нормалізований номер телефону
    """
    # Видаляємо всі символи крім цифр та +
    clean_number = re.sub(r"[^0-9+]", "", phone_number)

    # Якщо номер починається з 380, додаємо +
    if clean_number.startswith("380"):
        clean_number = "+" + clean_number
    # Якщо номер починається з 0, додаємо +38
    elif clean_number.startswith("0"):
        clean_number = "+38" + clean_number
    # Якщо номер не починається з +, додаємо +38
    elif not clean_number.startswith("+"):
        clean_number = "+38" + clean_number

    return clean_number
