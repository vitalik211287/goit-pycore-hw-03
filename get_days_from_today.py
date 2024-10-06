from datetime import datetime


date = "2021-05-05"


def get_days_from_today(date: str) -> int:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.strptime(str(datetime.now().date()), "%Y-%m-%d")  
        days_difference = current_date.toordinal() - given_date.toordinal()
        return days_difference
    except ValueError:
        return "Помилка: Невірний формат дати! Формат повинен бути YYYY-MM-DD."


print(get_days_from_today(date)) 






