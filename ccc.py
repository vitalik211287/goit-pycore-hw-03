from datetime import datetime, timedelta

# Список користувачів з днями народження
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "ssdasd asddas", "birthday": "2024.10.12"},
    {"name": "Vitalii Pol", "birthday": "2024.10.03"}
]

# Функція для визначення днів народження на наступний тиждень
def get_upcoming_birthdays(users):
    current_date = datetime.today().date()  # Поточна дата
    upcoming_birthdays = []  # Список для збереження результатів
    
    # Проходимо по кожному користувачу
    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()  # Конвертація дня народження
        
        # День народження у поточному році
        birthday_this_year = birthday_date.replace(year=current_date.year)
        
        # Якщо день народження вже пройшов, перевіряємо на наступний рік
        if birthday_this_year < current_date:
            birthday_this_year = birthday_date.replace(year=current_date.year + 1)
        
        # Різниця в днях між поточною датою і днем народження
        days_difference = (birthday_this_year - current_date).days
        
        # Якщо день народження на наступному тижні (включаючи сьогодні)
        if 0 <= days_difference <= 7:
            congratulation_date = birthday_this_year
            
            # Якщо день народження випадає на вихідні (субота або неділя)
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += timedelta(days=2)  # Переносимо на понеділок
            elif congratulation_date.weekday() == 6:  # Неділя
                congratulation_date += timedelta(days=1)  # Переносимо на понеділок
            
            # Додаємо користувача та дату привітання у список
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Виклик функції та виведення результату
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
