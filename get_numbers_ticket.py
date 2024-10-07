import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> int:
    
        
    try:
        # Перевірка чи всі аргументи є цілими числами
        if min != int(min) or  max != int(max) or quantity != int(quantity) :
            return TypeError("Усі вхідні дані повинні бути цілими числами.")
        
        # Перевірка, чи максимальне значення більше мінімального
        if min > max:
            return  ValueError("Мінімальне значення не може бути більше за максимальне.")
        
        # Перевірка, чи кількість значень менша максимального
        if  min > quantity  or quantity > max:
            return  ValueError("Кількість значення повинна бути в діапазоні між мінімальним та максимальним значеннями.")
        
        # Створення списку від мінімального до максимального числа
        list_numbers = list(range(min, max + 1))
        
        # Вибір випадкових чисел
        win_numbers = random.sample(list_numbers, k=quantity )

        # Сортування вибраних чисел
        win_numbers_sorted = sorted(win_numbers)
        return win_numbers_sorted

    except TypeError:  "Помилка: Невірний формат даних! " 
    
    

print(get_numbers_ticket(1, 1000, 5))


