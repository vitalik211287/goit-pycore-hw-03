from datetime import datetime


date = "2024-05-05"


def get_days_from_today(date: str) -> int:
    try:
        # Спроба перетворити рядок на дату у форматі "YYYY-MM-DD"
        given_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today().date() 
       
        # Обчислення різниці у днях
        days_difference = current_date.toordinal() - given_date.toordinal()
        return days_difference
    except ValueError:
       
        # Обробка помилки неправильного формату дати
        return "Помилка: Невірний формат дати! Формат повинен бути YYYY-MM-DD."


print(get_days_from_today(date)) 








