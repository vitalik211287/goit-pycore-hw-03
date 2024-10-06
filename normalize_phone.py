import re

def normalize_phone(phone_number: str) -> str:
    # Видаляємо всі символи, крім цифр і символу '+'
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    
    match phone_number:
            case number if number.startswith("380"):
                # Якщо номер починається з '380', додаємо лише '+'
                return f"+{number}"
            case number if number.startswith("+"):
                # Якщо номер вже має міжнародний код, залишаємо без змін
                return number
            case _:
                # Якщо немає міжнародного коду, додаємо код для України '+38'
                return f"+38{phone_number}"


print(normalize_phone('123456789'))


