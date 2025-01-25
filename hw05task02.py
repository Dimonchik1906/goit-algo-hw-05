import re
from typing import Callable, Generator 

def generator_numbers(text: str): # функція аналізу тексту та інденифікує всі дійсні числа
    pattern = r"(\s)(\d+\.\d+|\d+)(\s)"
    # sdfsf
    """
    Шаблон пошуку чисел, в якому:
    (\s) перед числом є пробіл
    (\d+\.\d+|\d+) знаходить числа з десятковою точкою(\d+\.\d+) або (|) ціле число (\d+)
    (s) після числа є пробіл
    """
    for match in re.finditer(pattern, text):  
        yield float(match.group(0)) # Використовую функцію yield для створення генератора

def sum_profit(text: str, func: Callable[[str], Generator[float]]):
    return sum(func(text)) # Cумуємо отримані результати
    
    


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

