from datetime import datetime, timedelta



users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "ssdasd asddas", "birthday": "2024.10.12"},
    {"name": "Vitalii Pol", "birthday": "2024.10.03"}
]


def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    upcoming_birthdays = []

# Проходимо по кожному користувачу
    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

# Якщо день народження вже пройшов, перевіряємо на наступний рік
        birthday_this_year = datetime(current_date.year, birthday_date.month,  birthday_date.day ).date()

# Якщо день народження вже пройшов, перевіряємо на наступний рік        
        if birthday_this_year < current_date:
            birthday_this_year = datetime(current_date.year + 1, birthday_date.month,  birthday_date.day ).date()

# Різниця в днях між поточною датою і днем народження       
        difference_days = birthday_this_year.toordinal()  - current_date.toordinal()

# Якщо день народження на наступному тижні (включаючи сьогодні)
        if 0 <= difference_days <= 7:
            congratulation_date = birthday_this_year

 # Якщо день народження випадає на вихідні (субота або неділя)
            if birthday_this_year.weekday() == 5 :
                congratulation_date += timedelta(days=2) 
            elif birthday_this_year.weekday() == 6:
                congratulation_date += timedelta(days=1)

    upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays


print(get_upcoming_birthdays(users))
